import asyncio
from multidict import CIMultiDict as _CIMultiDict
from typing import (
    Any, Type, Union, List, Dict, Optional, Mapping, Callable
)

from yarl import URL as _URL
from aiohttp import (
    ClientTimeout, ClientResponse, ClientSession as Session
)
from parsel.selector import Selector, SelectorList


__all__ = [
    "Url", "Urls", "Timeout", "Response", "AsyncSleep",
    "Headers", "EventLoop", "Semaphore", "Session", "RequestCallBack"
]


Url = Union[str, _URL]
Urls = Union[
    List[Url], List[List[Union[Url, Dict[str, Any]]]]
]
Timeout = Union[int, float, ClientTimeout]
Headers = Union[Dict[str, Any], _CIMultiDict]
EventLoop = asyncio.AbstractEventLoop
Semaphore = Union[int, asyncio.Semaphore]
AsyncSleep = Union[int, float]
RequestCallBack = Optional[Callable]
CbKwargs = Dict[str, Any]
CbKwargsList = Union[CbKwargs, List[CbKwargs]]


class Response(ClientResponse):

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

    def urljoin(self, url):
        """urljoin

        :param self: aiohttp.ClientResponse 实例
        :param url: url
        :return: yarl.URL
        """
