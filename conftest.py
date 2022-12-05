import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser tu run tests")
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"), help="browser drivers path")
    parser.addoption("--headless", action="store_true", help="browser tu run tests")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers_path = request.config.getoption("--drivers")
    url = request.config.getoption("--url")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers_path + "/chromedriver")
        driver = webdriver.Chrome(service=service)

    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=os.path.expanduser(f"{drivers_path}/yandexdriver"))
    elif browser == "firefox":
        service = FFService(executable_path=drivers_path + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")

    driver.maximize_window()
    driver.get(url)
    driver.url = url
    yield driver

    driver.close()
