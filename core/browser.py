from playwright.sync_api import BrowserContext as PlaywrightBrowserContext
from core.page import BrowserPageBase, PlaywrightPage


from abc import ABC, abstractmethod


class BrowserBase(ABC):
    @abstractmethod
    def new_page(self) -> BrowserPageBase:
        pass


class PlaywrightBrowser(BrowserBase):
    def __init__(self, playwright: PlaywrightBrowserContext) -> None:
        self.playwright = playwright

    def new_page(self) -> PlaywrightPage:
        return PlaywrightPage(page=self.playwright.new_page())
