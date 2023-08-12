import asyncio
from types import MethodType
from multidict import CIMultiDict
from typing import List, Union, Optional

from pyxk import default_headers
from pyxk.aclient.typedef import (
    Url, Urls, _URL, Session,
    Semaphore, EventLoop, Response, Timeout,
    ClientTimeout, AsyncSleep, Headers, ClientResponse
)


class BaseClient:

    limit: int = 100
    delay: AsyncSleep = 1
    timeout: Timeout = 10
    verify: bool = True
    warning: bool = True
    headers: Headers = CIMultiDict(default_headers())
    semaphore: Semaphore = 16
    user_agent: Optional[str] = None
    req_kwargs: dict = {}
    start_urls: Optional[Urls] = []
    max_retries: int = 10
    aiohttp_kwargs: dict = {}
    status_retry_list: List[int] = []
    status_error_list: List[int] = []
    until_request_succeed: Union[bool, List[int]] = False

    def __init__(
        self,
        *,
        loop: Optional[EventLoop] = None,
        base_url: Optional[Url] = None,
        **kwargs
    ) -> None:
        # event loop
        if loop is None:
            self._loop = asyncio.get_event_loop()
        elif isinstance(loop, asyncio.AbstractEventLoop):
            self._loop = loop
        else:
            raise ValueError(f"'loop' type must be a asyncio.AbstractEventLoop, got: {type(loop)}")
        asyncio.set_event_loop(self._loop)

        # aiohttp session
        self._session: Optional[Session] = None

        # base_url
        self._base_url: Optional[Url] = self.set_base_url(base_url)

        # 动态生成实例变量
        for key, val in kwargs.items():
            setattr(self, key, val)

        # 初始化
        self._initialization()

    def _initialization(self) -> None:
        # 无效 event loop
        if not isinstance(self.loop, asyncio.AbstractEventLoop):
            raise TypeError(f"'loop' type must be a asyncio.AbstractEventLoop, got: {type(self.loop)}")

        # 最大重试次数
        if not isinstance(self.max_retries, int) or self.max_retries <= 0:
            raise ValueError(f"'max_retries' initial value must be > 0, got: {self.max_retries}")

        # 状态码重试列表
        if not isinstance(self.status_retry_list, (list, tuple)):
            raise ValueError(f"'status_retry_list' type must be a list, got: {type(self.status_retry_list)}")

        # 状态码错误列表
        if not isinstance(self.status_error_list, (list, tuple)):
            raise ValueError(f"'status_retry_list' type must be a list, got: {type(self.status_error_list)}")

        # 直到请求成功
        if not isinstance(self.until_request_succeed, (list, tuple)):
            self.until_request_succeed = [200] if self.until_request_succeed else []

        # 异步休眠
        if not isinstance(self.delay, (int, float)) or self.delay < 0:
            raise ValueError(f"'delay' initial value must be >= 0, got: {self.delay}")

        # semaphore
        if not isinstance(self.semaphore, asyncio.Semaphore):
            if not isinstance(self.semaphore, int):
                raise TypeError(f"'semaphore' type must be a int or asyncio.Semaphore, got: {type(self.semaphore)}")
            if self.semaphore <= 0:
                raise ValueError(f"'semaphore' initial value must be > 0, got: {self.semaphore}")

        # aiohttp_kwargs
        if not isinstance(self.aiohttp_kwargs, dict):
            raise TypeError(f"'aiohttp_kwargs' type must be a dict, got: {type(self.aiohttp_kwargs)}")

        # timeout
        if not isinstance(self.timeout, ClientTimeout):
            if not isinstance(self.timeout, (int, float)):
                raise TypeError(f"'timeout' type must be a str or float or aiohttp.ClientTimeout, got: {type(self.semaphore)}")
            if self.timeout < 0:
                raise ValueError(f"'timeout' initial value must be >= 0, got: {self.timeout}")

        # limit
        if not isinstance(self.limit, int) or self.limit <= 0:
            raise ValueError(f"'limit' initial value must be > 0, got: {self.limit}")

        # headers
        if not isinstance(self.headers, (dict, CIMultiDict)):
            raise TypeError(f"'headers' type must be a dict or CIMultiDict, got: {type(self.headers)}")
        # --headers.user_agent
        if not isinstance(self.user_agent, str) and self.user_agent is not None:
            raise TypeError(f"'user_agent' type must be a str, got: {type(self.user_agent)}")

        # req_kwargs
        if not isinstance(self.req_kwargs, dict):
            raise TypeError(f"'req_kwargs' type must be a dict, got: {type(self.req_kwargs)}")

    async def completed(self, result: list) -> None:
        """运行完成结果回调函数"""

    async def open(self) -> None:
        """创建 aiohttp session 之前调用"""

    async def close(self) -> None:
        """关闭 aiohttp session 之后调用"""

    async def start(self) -> None:
        """创建 aiohttp session 之后调用"""

    async def stop(self) -> None:
        """关闭 aiohttp session 之前调用"""

    @staticmethod
    def set_base_url(url: Url) -> Optional[Url]:
        """设置 base_url"""
        if url is None:
            return None
        if not isinstance(url, (str, _URL)):
            raise TypeError(f"'base_url' type must be a str or yarl.URL, got: {type(url)}")

        url = _URL(url)
        if url.is_absolute():
            return url
        return None

    @property
    def loop(self) -> EventLoop:
        """event loop"""
        return self._loop

    @property
    def session(self) -> Session:
        """aiohttp session"""
        return self._session

    @property
    def base_url(self) -> Optional[Url]:
        """base_url"""
        return self._base_url

    @base_url.setter
    def base_url(self, _url: Url) -> None:
        self._base_url = self.set_base_url(_url)


def add_instance_method(response):
    """为异步response添加实例方法"""
    method_list = set(dir(Response)) - set(dir(ClientResponse))
    for item in method_list:
        setattr(response, item, MethodType(getattr(Response, item), response))
