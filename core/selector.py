from enum import StrEnum
from typing import TypeAlias, Tuple


class By(StrEnum):
    XPATH = "xpath"
    CSS_SELECTOR = "css selector"
    ID = "id"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"


Selector: TypeAlias = Tuple[By, str]


def qa_selector(value: str) -> Selector:
    return By.CSS_SELECTOR, f'[qa-attribute="{value}"]'
