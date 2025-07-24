from abc import ABC, abstractmethod

from playwright.sync_api import Locator
from core.selector import Selector


class LocatorDescriptor:
    def __init__(self, selector: Selector, name):
        self.selector = selector
        self.element_name = name

    def __get__(self, page_obj, owner):
        from pages.page_object import PageObjectBase

        if page_obj is None or not isinstance(page_obj, PageObjectBase):
            raise TypeError(
                "LocatorDescriptor must be defined as a class attribute inside a page object class, not used elsewhere."
            )

        return page_obj.page.get_locator(
            selector=self.selector,
            page_name=page_obj.page_name,
            name=self.element_name,
        )


class LocatorBase(ABC):
    def __init__(self, selector: Selector, page, page_name, element_name) -> None:
        self.selector = selector
        self.by = selector[0]
        self.locator = selector[1]
        self._page = page
        self.page_name = page_name
        self.element_name = element_name

    @abstractmethod
    def click(self) -> None: ...

    @abstractmethod
    def wait_visible(self) -> None: ...


class PlaywrightLocator(LocatorBase):
    @property
    def _element(self) -> Locator:
        return self._page.locator(self.locator)  # обработка by

    def click(self) -> None:
        self._element.click()

    def wait_visible(self) -> None:
        self._element.wait_for(state="visible")
