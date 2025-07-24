from enum import StrEnum
from core.selector import qa_selector
from core.locator import LocatorDescriptor
from pages.page_object import PageObjectBase
from core.page import BrowserPageBase


class CardButton(StrEnum):
    TITLE = "title"
    LEVEL = "level"
    CHECKBOX = "checkbox"
    PRACTICE_BUTTON = "practice-button"
    DETAILS_BUTTON = "details-button"


class Card(PageObjectBase):
    def __init__(self, number: int, page: BrowserPageBase) -> None:
        super().__init__(page)
        self.number = number

    def get_element_by_button(self, button: CardButton):
        return self.get_locator(
            selector=qa_selector(f"card{self.number}-{button}"),
            name=f"card{self.number}_{button}",
        )

    @property
    def title(self):
        return self.get_element_by_button(CardButton.TITLE)

    @property
    def level(self):
        return self.get_element_by_button(CardButton.LEVEL)

    @property
    def checkbox(self):
        return self.get_element_by_button(CardButton.CHECKBOX)

    @property
    def practice_button(self):
        return self.get_element_by_button(CardButton.PRACTICE_BUTTON)

    @property
    def details_button(self):
        return self.get_element_by_button(CardButton.DETAILS_BUTTON)


class FearListPage(PageObjectBase):
    page_name = "FearListPage"

    add_fear_button = LocatorDescriptor(
        selector=qa_selector("add-fear-button"),
        name="add_fear_button",
    )

    def get_card_obj(self, number: int) -> Card:
        return Card(page=self.page, number=number)
