import os
import logging
import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser tu run tests")
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"), help="browser drivers path")
    parser.addoption("--headless", action="store_true", help="browser tu run tests")
    parser.addoption("--main_url", action="store", default="http://172.16.16.20:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers_path = request.config.getoption("--drivers")
    main_url = request.config.getoption("--main_url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

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
    driver.get(main_url)
    driver.main_url = main_url
    driver.log_level = log_level
    driver.logger = logger

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    yield driver

    driver.close()
