from abc import ABC, abstractmethod

from playwright.sync_api import Page

from core.locator import PlaywrightLocator
from core.locator import LocatorBase
from core.selector import Selector


class BrowserPageBase(ABC):
    @abstractmethod
    def goto(self, url: str) -> None: ...

    @abstractmethod
    def get_locator(
        self, selector: Selector, page_name: str, name: str
    ) -> LocatorBase: ...


class PlaywrightPage(BrowserPageBase):
    def __init__(self, page: Page) -> None:
        self.__page = page

    def goto(self, url: str) -> None:
        self.__page.goto(url=url)

    def get_locator(
        self, selector: Selector, page_name: str, name: str
    ) -> PlaywrightLocator:
        return PlaywrightLocator(
            selector=selector,
            page=self.__page,
            page_name=page_name,
            element_name=name,
        )
