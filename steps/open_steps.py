import allure
from core.settings import Config


class OpenSteps:
    def __init__(self, page, config: Config):
        self.page = page
        self.config = config

    @allure.step("Open main page")
    def open_main_page(self) -> None:
        self.page.goto(self.config.test.base_url) 