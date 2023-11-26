"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1536, 864), (360, 800), (390, 844)])
def browser_size(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param[0] >= 1012:
        return "desktop"
    else:
        return "mobile"


def test_github_desktop(browser_size):
    if browser_size != "desktop":
        pytest.skip(reason="Run on desktop only")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))


def test_github_mobile(browser_size):
    if browser_size != "mobile":
        pytest.skip(reason="Run on mobile only")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))
