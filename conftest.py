import pytest
import os
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser tu run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser tu run tests"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.headless = True
        _driver = webdriver.Chrome(
            executable_path=os.path.expanduser("~/drivers/chromedriver"),
            options=options
        )
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser("~/drivers/geckodriver"))
    elif browser_name == "opera":
        _driver = webdriver.Opera(executable_path=os.path.expanduser("~/drivers/operadriver"))
    elif browser_name == "yandex":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser("~/drivers/yandexdriver"))
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    yield _driver

    _driver.close()
