from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from core.page import BrowserPageBase
from core.selector import Selector
from core.locator import LocatorBase

if TYPE_CHECKING:
    pass


class PageObjectBase(ABC):
    page_name = "PageName"

    def __init__(self, page: BrowserPageBase) -> None:
        self.page = page

    def get_locator(self, selector: Selector, name: str) -> LocatorBase:
        return self.page.get_locator(
            selector=selector,
            page_name=self.page_name,
            name=name,
        )
