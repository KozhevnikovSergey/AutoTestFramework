import pytest

from core.context import TestContext
from steps.fears_list_steps import FearsListSteps
from steps.open_steps import OpenSteps


@pytest.fixture(scope="function")
def fears_list_steps(test_context: TestContext) -> FearsListSteps:
    return FearsListSteps(page=test_context.page)


@pytest.fixture(scope="function")
def open_steps(test_context: TestContext) -> OpenSteps:
    return OpenSteps(page=test_context.page, config=test_context.config)
