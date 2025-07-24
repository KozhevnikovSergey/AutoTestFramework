import allure
from pages.fear_list_page import FearListPage, CardButton


class FearsListSteps:
    def __init__(self, page):
        self.page = FearListPage(page)

    @allure.step("Verify all card buttons are present for card {card_number}")
    def verify_card_buttons_are_present(self, card_number: int) -> None:
        card = self.page.get_card_obj(card_number)

        for button in CardButton:
            card.get_element_by_button(button).wait_visible()

    @allure.step("Click card button {button} for card {card_number}")
    def click_card_button(self, card_number: int, button: CardButton) -> None:
        card = self.page.get_card_obj(card_number)
        element = card.get_element_by_button(button)
        element.click()

    @allure.step("Verify card button {button} is visible for card {card_number}")
    def verify_card_button_visible(self, card_number: int, button: CardButton) -> None:
        card = self.page.get_card_obj(card_number)
        element = card.get_element_by_button(button)
        element.wait_visible()
