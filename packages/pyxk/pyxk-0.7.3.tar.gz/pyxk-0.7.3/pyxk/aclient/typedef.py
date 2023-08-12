import asyncio
from multidict import CIMultiDict as _CIMultiDict
from typing import (
    Any, Union, List, Dict, Optional, Mapping, Callable, Tuple
)

from yarl import URL as _URL
from aiohttp import (
    ClientTimeout,
    ClientResponse,
    ClientSession as Session
)
from parsel.selector import Selector, SelectorList

from pyxk.utils import chardet


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

    async def _initi_text(self, encoding: Optional[str] = None) -> Tuple[str, str]:
        """解析 text & encoding"""
        try:
            encoding = encoding or self.get_encoding()
            text = await self.text(encoding)
        except UnicodeError:
            text = await self.read()
            encoding = chardet(text).encoding or "utf-8"
            text = text.decode(encoding, errors="ignore")

        return text, encoding

    async def xpath(
        self,
        query: str,
        type: Optional[str] = None,
        encoding: Optional[str] = None,
        base_url: Optional[str] = None,
        namespaces: Optional[Mapping[str, str]] = None,
    ) -> SelectorList[Selector]:
        """selector.xpath

        :param query: xpath查询字符串
        :param type: 文件类型 - "html"(default), "json", or "xml"
        :param encoding: text encoding
        :param base_url: 为文档设置URL
        :param namespaces: `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
            for additional prefixes to those registered with `register_namespace(prefix, uri)`.
            Contrary to `register_namespace()`, these prefixes are not
            saved for future calls.
        """
        text, encoding = await self._initi_text(encoding)
        # selector
        sel = Selector(
            text=text,
            type=type,
            base_url=base_url,
            encoding=encoding,
            namespaces=namespaces
        )
        # xpath
        return sel.xpath(query=query)

    async def css(
        self,
        query: str,
        type: Optional[str] = None,
        encoding: Optional[str] = None,
        base_url: Optional[str] = None,
        namespaces: Optional[Mapping[str, str]] = None,
    ) -> SelectorList[Selector]:
        """selector.css

        :param query: xpath查询字符串
        :param type: 文件类型 - "html"(default), "json", or "xml"
        :param encoding: text encoding
        :param base_url: 为文档设置URL
        :param namespaces:
            `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
            for additional prefixes to those registered with `register_namespace(prefix, uri)`.
            Contrary to `register_namespace()`, these prefixes are not
            saved for future calls.
        """
        text, encoding = await self._initi_text(encoding)
        # selector
        sel = Selector(
            text=text,
            type=type,
            base_url=base_url,
            encoding=encoding,
            namespaces=namespaces
        )
        # css
        return sel.css(query=query)

    async def re(
        self,
        regex: str,
        type: Optional[str] = None,
        encoding: Optional[str] = None,
        base_url: Optional[str] = None,
        namespaces: Optional[Mapping[str, str]] = None,
        replace_entities: bool = True,
    ) -> List[str]:
        """selector.re

        :param regex: 编译的正则表达式 或者 字符串
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
        text, encoding = await self._initi_text(encoding)
        # selector
        sel = Selector(
            text=text,
            type=type,
            base_url=base_url,
            encoding=encoding,
            namespaces=namespaces
        )
        # re
        return sel.re(regex=regex, replace_entities=replace_entities)

    async def selector(
        self,
        type: Optional[str] = None,
        encoding: Optional[str] = None,
        base_url: Optional[str] = None,
        namespaces: Optional[Mapping[str, str]] = None,
        **kwargs
    ) -> Selector:
        """selector

        :param regex: 编译的正则表达式 或者 字符串
        :param type: 文件类型 - "html"(default), "json", or "xml"
        :param encoding: text encoding
        :param base_url: 为文档设置URL
        :param namespaces:
            `namespaces` is an optional `prefix: namespace-uri` mapping (dict)
            for additional prefixes to those registered with `register_namespace(prefix, uri)`.
            Contrary to `register_namespace()`, these prefixes are not
            saved for future calls.
        """
        text, encoding = await self._initi_text(encoding)
        return Selector(
            text=text,
            type=type,
            base_url=base_url,
            encoding=encoding,
            namespaces=namespaces,
            **kwargs
        )

    def urljoin(self, url: Url, **kw) -> Url:
        """yarl.URL - urljoin"""
        if not isinstance(url, (str, _URL)):
            raise TypeError(f"'url' must be a str or yarl.URL, got: {type(url)}")
        url = _URL(url, **kw)
        if url.is_absolute():
            return url
        return self.url.join(url)
