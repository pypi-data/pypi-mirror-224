import asyncio
from types import MethodType
from multidict import CIMultiDict
from typing import Any, List, Union, Optional, Mapping

from pyxk import default_headers, chardet
from pyxk.aclient.typedef import (
    Url, Timeout, Headers, Semaphore, _URL, ClientTimeout,
    Urls, AsyncSleep, EventLoop, Session, Response, Selector
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

    async def parse(self, response: Response, **kwargs):
        """默认解析函数"""
        raise NotImplementedError(f"'{self.__class__.__name__}.parse' not implemented")

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

    async def sleep(self, delay: Optional[AsyncSleep] = None, result: Any = None):
        """异步休眠

        :param delay: 休眠时间
        :param result: 返回值
        :return: result
        """
        if delay is None:
            delay = self.delay
        elif not isinstance(delay, (int, float)) or delay < 0:
            raise ValueError(f"'delay' initial value must be >= 0, got: {delay}")

        return await asyncio.sleep(delay, result=result)

    def build_url(self, url: Url) -> Url:
        """构造完整url地址"""
        if not isinstance(url, (str, _URL)):
            raise TypeError(f"'url' type must be a str or yarl.URL, got: {type(url)}")

        url = _URL(url)
        if (
            url.is_absolute()
            or not isinstance(self.base_url, _URL)
        ):
            return url
        return self.base_url.join(url)

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


async def xpath(
    self,
    query: str,
    text: Optional[str] = None,
    type: Optional[str] = None,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
    namespaces: Optional[Mapping[str, str]] = None,
):
    """selector.xpath

    :param self: aiohttp.ClientResponse 实例
    :param query: xpath查询字符串
    :param text: str对象
    :param type: 文件类型 - "html"(default), "json", or "xml"
    :param encoding: text encoding
    :param base_url: 为文档设置URL
    :param namespaces: `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
        for additional prefixes to those registered with `register_namespace(prefix, uri)`.
        Contrary to `register_namespace()`, these prefixes are not
        saved for future calls.
    """
    try:
        if not text:
            text = await self.text(encoding)

    except UnicodeError:
        text = await self.read()
        encoding = chardet(text).encoding
        text = text.decode(encoding, errors="ignore")

    # selector
    sel = Selector(
        text=text,
        type=type,
        base_url=base_url,
        encoding=encoding or self.get_encoding(),
        namespaces=namespaces
    )
    # xpath
    return sel.xpath(query=query)


async def css(
    self,
    query: str,
    text: Optional[str] = None,
    type: Optional[str] = None,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
    namespaces: Optional[Mapping[str, str]] = None,
):
    """selector.css

    :param self: aiohttp.ClientResponse 实例
    :param query: xpath查询字符串
    :param text: str对象
    :param type: 文件类型 - "html"(default), "json", or "xml"
    :param encoding: text encoding
    :param base_url: 为文档设置URL
    :param namespaces:
        `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
        for additional prefixes to those registered with `register_namespace(prefix, uri)`.
        Contrary to `register_namespace()`, these prefixes are not
        saved for future calls.
    """
    try:
        if not text:
            text = await self.text(encoding)

    except UnicodeError:
        text = await self.read()
        encoding = chardet(text).encoding
        text = text.decode(encoding, errors="ignore")

    # selector
    sel = Selector(
        text=text,
        type=type,
        base_url=base_url,
        encoding=encoding or self.get_encoding(),
        namespaces=namespaces
    )
    # css
    return sel.css(query=query)


async def re(
    self,
    regex: str,
    text: Optional[str] = None,
    type: Optional[str] = None,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
    namespaces: Optional[Mapping[str, str]] = None,
    replace_entities: bool = True,
):
    """selector.re

    :param self: aiohttp.ClientResponse 实例
    :param regex: 编译的正则表达式 或者 字符串
    :param text: str对象
    :param type: 文件类型 - "html"(default), "json", or "xml"
    :param encoding: text encoding
    :param base_url: 为文档设置URL
    :param namespaces:
        `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
        for additional prefixes to those registered with `register_namespace(prefix, uri)`.
        Contrary to `register_namespace()`, these prefixes are not
        saved for future calls.
    :param replace_entities:
        By default, character entity references are replaced by their
        corresponding character (except for ``&amp;`` and ``&lt;``).
        Passing ``replace_entities`` as ``False`` switches off these
        replacements.
    """
    try:
        if not text:
            text = await self.text(encoding)

    except UnicodeError:
        text = await self.read()
        encoding = chardet(text).encoding
        text = text.decode(encoding, errors="ignore")

    # selector
    sel = Selector(
        text=text,
        type=type,
        base_url=base_url,
        encoding=encoding or self.get_encoding(),
        namespaces=namespaces
    )
    # re
    return sel.re(regex=regex, replace_entities=replace_entities)


async def selector(
    self,
    text: Optional[str] = None,
    type: Optional[str] = None,
    encoding: Optional[str] = None,
    base_url: Optional[str] = None,
    namespaces: Optional[Mapping[str, str]] = None,
    **kwargs
):
    """selector

    :param self: aiohttp.ClientResponse 实例
    :param regex: 编译的正则表达式 或者 字符串
    :param text: str对象
    :param type: 文件类型 - "html"(default), "json", or "xml"
    :param encoding: text encoding
    :param base_url: 为文档设置URL
    :param namespaces:
        `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
        for additional prefixes to those registered with `register_namespace(prefix, uri)`.
        Contrary to `register_namespace()`, these prefixes are not
        saved for future calls.
    """
    try:
        if not text:
            text = await self.text(encoding)

    except UnicodeError:
        text = await self.read()
        encoding = chardet(text).encoding
        text = text.decode(encoding, errors="ignore")

    return Selector(
        text=text,
        type=type,
        base_url=base_url,
        encoding=encoding or self.get_encoding(),
        namespaces=namespaces,
        **kwargs
    )


def urljoin(self, url):
    """urljoin

    :param self: aiohttp.ClientResponse 实例
    :param url: url
    :return: yarl.URL
    """
    if not isinstance(url, (str, _URL)):
        raise TypeError(f"'url' must be a str or yarl.URL, got: {type(url)}")

    url = _URL(url)
    if url.is_absolute():
        return url
    return self.url.join(url)


def add_instance_method(response):
    """为异步response添加实例方法 - re, css, xpath, urljoin"""
    setattr(response, 're', MethodType(re, response))
    setattr(response, 'css', MethodType(css, response))
    setattr(response, 'xpath', MethodType(xpath, response))
    setattr(response, 'urljoin', MethodType(urljoin, response))
    setattr(response, 'selector', MethodType(selector, response))
