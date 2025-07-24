import pytest

from core.settings import Config, Platform
from core.context import PlaywrightContextFactory, TestContext

pytest_plugins = ["steps.conftest"]


@pytest.fixture(scope="session")
def config() -> Config:
    return Config.load_from_yaml()


@pytest.fixture(scope="session")
def test_context(config: Config) -> TestContext:
    match config.environment.platform:
        # case Platform.MOBILE:
        #     ContextFactory = AppiumContextFactory
        case Platform.WEB:
            ContextFactory = PlaywrightContextFactory
        case _:
            raise Exception(
                f"Unknown platform '{config.environment.platform}' in config"
            )

    return ContextFactory(config=config).build_test_context()
