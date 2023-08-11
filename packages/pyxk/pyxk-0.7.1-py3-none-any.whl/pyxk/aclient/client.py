import logging
import asyncio
from typing import (
    Any, List, Union, Optional, Dict, Tuple
)
from multidict import CIMultiDict

from aiohttp import ClientTimeout, ClientSession, TCPConnector
from aiohttp.client_exceptions import (
    ClientError,
    ClientOSError,
    ClientPayloadError,
    ClientConnectorError,
    ServerDisconnectedError
)

from pyxk.aclient._base import BaseClient, add_instance_method
from pyxk.aclient.typedef import (
    _URL,
    Url,
    Urls,
    Session,
    Headers,
    Timeout,
    CbKwargs,
    Response,
    Semaphore,
    CbKwargsList,
    RequestCallBack
)


class Client(BaseClient):
    """异步下载器

    explain:
    from pyxk import Client, Response

    class Download(Client):
        start_urls = ['http://www.baidu.com' for _ in range(10)]

        async def parse(self, response: Response, **kwargs):
            print(response.url)

    Download.run()
    """
    async def async_start(self) -> None:
        """开启异步下载器"""
        try:
            await self.open()

            # semaphore
            if not isinstance(self.semaphore, asyncio.Semaphore):
                self.semaphore: Semaphore = asyncio.Semaphore(self.semaphore)

            # aiohttp timeout(超时时间)
            if not isinstance(self.timeout, ClientTimeout):
                self.timeout: Timeout = ClientTimeout(total=self.timeout)

            # aiohttp connector(连接器)
            connector = TCPConnector(
                limit=self.limit, ssl=bool(self.verify), loop=self.loop
            )

            # aiohttp headers
            self.headers: Headers = CIMultiDict(self.headers)
            # -- headers.user_agent
            if isinstance(self.user_agent, str):
                self.headers["User-Agent"] = self.user_agent

            try:
                # 创建 aiohttp.ClientSession
                self._session: Session = ClientSession(
                    loop=self.loop,
                    connector=connector,
                    timeout=self.timeout,
                    headers=self.headers,
                    **self.aiohttp_kwargs
                )
                await self.start()

                # 运行 start_request
                result = await self.start_request()
                await self.completed(result)

            finally:
                await self.stop()
                # 关闭 aiohttp.ClientSession
                if self.session:
                    await self.session.close()
        finally:
            await self.close()

    async def start_request(
        self,
        callback: Optional[RequestCallBack] = None,
        set_base_url: Union[str, bool] = True,
        **kwargs
    ) -> list:
        """start_urls 默认运行方法

        :param callback: 回调函数
        :param set_base_url: 设置base url
        :return: list
        """
        if (
            not self.start_urls
            or not isinstance(self.start_urls, (list, tuple))
        ):
            raise NotImplementedError(
                f"'{self.__class__.__name__}.start_urls' not implemented, got: {self.start_urls}"
            )

        kwargs.update(self.req_kwargs)

        return await self.gather(
            urls=self.start_urls,
            callback=callback if callable(callback) else self.parse,
            set_base_url=set_base_url,
            **kwargs
        )

    async def gather(
        self,
        urls: Urls,
        callback: Optional[RequestCallBack] = None,
        *,
        method: str = "GET",
        set_base_url: Union[bool, str] = False,
        cb_kwargs_list: CbKwargsList = {},
        return_exceptions: bool = False,
        **kwargs
    ) -> list:
        """发送url列表，创建异步任务 并发发送

        :param urls: Url List
        :param callback: 响应response 回调函数(函数是异步的)
        :param method: 请求方法(default: GET)
        :param set_base_url: 是否设置base_url
        :param cb_kwargs_list: 回调函数关键字参数列表
        :param return_exceptions: 错误传递(default: False)
        :return: list
        """
        if not isinstance(urls, (list, tuple)):
            raise TypeError(f"'urls' type must be a list, got: {type(urls)}")

        cb_kwargs_list = self._cb_kwargs_list(cb_kwargs_list, len(urls))

        # urls
        for index, item in enumerate(urls):
            url, cb = None, {}
            # 每项为列表
            if item and isinstance(item, (list, tuple)):
                if len(item) == 1:
                    url = item[0]
                if len(item) >= 2:
                    url = item[0]
                    try:
                        cb = dict(item[1]).copy()
                    except TypeError as e:
                        raise TypeError(
                            "'urls' each item value must be a "
                            f"Url or List[Union[Url, Dict[str, Any]]], got: {item}"
                        ) from e
            # 每项为字符串
            elif isinstance(item, (str, _URL)):
                url = item
            else:
                raise TypeError(
                    "'urls' each item value must be a "
                    f"Url or List[Union[Url, Dict[str, Any]]], got: {item}"
                )

            # 更新数据
            urls[index] = url
            cb.update(cb_kwargs_list[index])
            cb_kwargs_list[index] = cb

        # 设置 base url
        if set_base_url:
            # 链接
            if (
                isinstance(set_base_url, str)
                and set_base_url.startswith(("http://", "https://"))
            ):
                self.base_url = set_base_url
            # 自动设置
            elif not self.base_url:
                from urllib.parse import urljoin
                self.base_url = urljoin(str(urls[0]), ".")

        # 创建异步任务
        requests_tasks = [
            self.request(
                url=url,
                callback=callback,
                method=method,
                cb_kwargs=cb_kwargs,
                **kwargs
            )
            for url, cb_kwargs in zip(urls, cb_kwargs_list)
        ]
        return await asyncio.gather(*requests_tasks, return_exceptions=return_exceptions)

    @staticmethod
    def _cb_kwargs_list(cb_kwargs_list: CbKwargsList, length: int) -> List[CbKwargs]:
        """解析回调函数参数 - cb_kwargs_list"""
        if not isinstance(cb_kwargs_list, (dict, list, tuple)):
            raise TypeError(f"'cb_kwargs_list' type must be a dict or list, got: {type(cb_kwargs_list)}")

        # 列表格式
        if isinstance(cb_kwargs_list, (list, tuple)):
            cb_kwargs_list = list(cb_kwargs_list)[:length]
            # 回调函数参数 每一项必须是字典
            for item in cb_kwargs_list:
                if not isinstance(item, dict):
                    raise TypeError(f"'cb_kwargs_list' each item type must be a dict, got: {type(item)}")

            if len(cb_kwargs_list) < length:
                cb_kwargs_list.extend(
                    [{} for _ in range(length-len(cb_kwargs_list))]
                )
            return cb_kwargs_list

        # 字典格式
        return [cb_kwargs_list for _ in range(length)]

    async def request(
        self,
        url: Url,
        callback: Optional[RequestCallBack] = None,
        *,
        method: str = "GET",
        cb_kwargs: CbKwargs = {},
        **kwargs
    ) -> Union[Response, Any]:
        """异步请求发送以及回调

        :param url: URL
        :param callback: 响应response 回调函数(函数是异步的)
        :param method: 请求方法(default: GET)
        :param cb_kwargs: 传递给回调函数的关键字参数
        :param kwargs: 异步请求 request参数
            params, data, json, cookies, headers,
            skip_auto_headers, auth, allow_redirects,
            max_redirects, compress, chunked, expect100,
            raise_for_status, read_until_eof, proxy, proxy_auth,
            timeout, verify_ssl, fingerprint,
            ssl_context, ssl, proxy_headers,
            trace_request_ctx, read_bufsize
        :return: Response, Any
        """
        if not isinstance(cb_kwargs, dict):
            raise TypeError(f"'cb_kwargs' type must be a dict, got: {type(cb_kwargs)}")

        url, ret, exc, response = self.build_url(url), None, None, None
        # 警告消息 确保只会警告一次
        warning = {
            "retry": True and self.warning,
            "succeed": True and self.warning,
            "timeout": True and self.warning,
            "client": True and self.warning,
            "disconnected": True and self.warning
        }

        async with self.semaphore:
            for _ in range(1, self.max_retries+1):
                try:
                    _continue, response = await self._send(
                        method=method, url=url, warning=warning, **kwargs
                    )
                    if _continue:
                        continue

                    add_instance_method(response)
                    # 开启回调函数
                    ret = response
                    if callable(callback):
                        ret = await callback(response, **cb_kwargs)
                    break

                # 请求超时 重试
                except asyncio.exceptions.TimeoutError as e:
                    # 提示信息
                    exc = e
                    await self._warn(
                        f"<{method.upper()} {url.human_repr()}> TimeoutError",
                        "timeout", warning
                    )
                # 连接错误 重试
                except (ClientOSError, ClientPayloadError, ClientConnectorError) as e:
                    exc = e
                    await self._warn(
                        f"<{method.upper()} {url.human_repr()}> ClientError",
                        "client", warning
                    )
                # 服务器拒绝连接
                except ServerDisconnectedError as e:
                    exc = e
                    await self._warn(
                        f"<{method.upper()} {url.human_repr()}> ServerDisconnectedError",
                        "disconnected", warning
                    )
                finally:
                    if response and callable(callback):
                        response.close()
            else:
                if exc:
                    raise exc
                # 达到最大请求次数
                raise RuntimeError(f"<{method.upper()} {url.human_repr()}>, max_retries: {self.max_retries}")

            return ret

    async def _send(
        self, method: str, url: Url, warning: Dict[str, bool], **kwargs
    ) -> Tuple[bool, Response]:
        """发送异步请求"""
        response = await self.session.request(method=method, url=url, **kwargs)
        request_status = {
            "continue": False,
            "status_retry_list": self.status_retry_list,
            "status_error_list": self.status_error_list
        }

        # until_request_succeed
        self._until_request_succeed(response, request_status)
        if request_status["continue"]:
            # 警告消息
            method = response.method.upper()
            await self._warn(
                f"<{method}[{response.status}] {response.url.human_repr()}>"
                f" be in until_request_succeed: {self.until_request_succeed}",
                "succeed", warning
            )
            return request_status["continue"], response

        # status_error_list
        if response.status in request_status["status_error_list"]:
            method = response.method.upper()
            raise ClientError(f"<{method}[{response.status}] {response.url.human_repr()}>")

        # status_retry_list
        if response.status in request_status["status_retry_list"]:
            request_status["continue"] = True
            # 警告消息
            method = response.method.upper()
            await self._warn(
                f"<{method}[{response.status}] {response.url.human_repr()}>"
                f" be in status_retry_list: {self.status_retry_list}",
                "retry", warning
            )
        return request_status["continue"], response

    def _until_request_succeed(
        self, response: Response, request_status: dict
    ) -> None:
        """状态码直到请求成功"""
        if not self.until_request_succeed:
            return

        if response.status in self.until_request_succeed:
            request_status["status_retry_list"] = []
            request_status["status_error_list"] = []
        else:
            request_status["continue"] = True
            # 错误状态码
            if response.status in self.status_error_list:
                method = response.request_info.method.upper()
                raise ClientError(f"<{method}[{response.status}] {response.url.human_repr()}>")

    async def _warn(self, text: str, key: str, warning: Dict[str, bool]) -> None:
        """request: 发出警告"""
        if warning[key]:
            logging.warning(text)
        # 确保只会警告一次
        warning[key] = False
        await self.sleep()

    @classmethod
    def run(cls, **kwargs) -> "Client":
        """程序运行入口 - 应该调用该方法运行"""
        kwargs.setdefault("loop", asyncio.new_event_loop())
        self = cls(**kwargs)

        # 运行
        self.loop.run_until_complete(self.async_start())

        # 关闭 EventLoop
        if self.loop:
            self.loop.close()
            asyncio.set_event_loop(None)

        return self

    async def parse(self, response: Response, **kwargs):
        """默认解析函数"""
        raise NotImplementedError(f"'{self.__class__.__name__}.parse' not implemented")
