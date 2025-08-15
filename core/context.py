from abc import ABC, abstractmethod
from dataclasses import dataclass

from playwright.sync_api import sync_playwright

from core.browser import BrowserBase, PlaywrightBrowser
from core.page import BrowserPageBase, PlaywrightPage
from core.settings import Config


@dataclass
class TestContext:
    browser: any
    page: any
    config: Config


class ContextFactory(ABC):
    def __init__(self, config: Config) -> None:
        self.config = config

    @abstractmethod
    def create_browser(self) -> BrowserBase:
        pass

    @abstractmethod
    def create_page(self, browser) -> BrowserPageBase:
        pass

    def build_test_context(self) -> TestContext:
        browser = self.create_browser()
        return TestContext(
            browser=browser,
            page=self.create_page(browser=browser),
            config=self.config,
        )


class PlaywrightContextFactory(ContextFactory):
    def create_browser(self) -> PlaywrightBrowser:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(
            headless=self.config.browser.headless,
        )

        return PlaywrightBrowser(
            playwright=browser.new_context(
                **playwright.devices[self.config.browser.device.type]
            )
        )

    def create_page(self, browser) -> PlaywrightPage:
        return browser.new_page()
