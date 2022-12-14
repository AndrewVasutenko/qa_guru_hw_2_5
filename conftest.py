import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.browser_name = 'chrome'
    yield
