import pytest
import os
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser tu run tests"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser("~/drivers"), help="browser drivers path"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser tu run tests"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers_path = request.config.getoption("--drivers")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.headless = True
        _driver = webdriver.Chrome(
            executable_path=os.path.expanduser(f"{drivers_path}/chromedriver"),
            options=options
        )
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser(f"{drivers_path}/geckodriver"))
    elif browser_name == "opera":
        _driver = webdriver.Opera(executable_path=os.path.expanduser(f"{drivers_path}/operadriver"))
    elif browser_name == "yandex":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser(f"{drivers_path}/yandexdriver"))
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    yield _driver

    _driver.close()
