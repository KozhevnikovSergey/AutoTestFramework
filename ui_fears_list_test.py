import allure

from steps.fears_list_steps import FearsListSteps


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Web interface")
@allure.feature("Buttons of the card")
def test_displaying_fear_card_on_window_load(fears_list_steps: FearsListSteps):
    fears_list_steps.verify_card_buttons_are_present(card_number=1)
