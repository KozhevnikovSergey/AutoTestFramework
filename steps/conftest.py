import pytest

from core.context import TestContext
from steps.fears_list_steps import FearsListSteps


@pytest.fixture(scope="function")
def fears_list_steps(test_context: TestContext) -> FearsListSteps:
    return FearsListSteps(page=test_context.page)
