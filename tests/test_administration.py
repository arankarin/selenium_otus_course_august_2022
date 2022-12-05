import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    """Проверка заголовка страницы"""
    browser.get(browser.url + "/administration/")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.title_is("Administration"))


def test_forgotten_password(browser):
    browser.get(browser.url + "/administration/")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="mb-3"]>a'))).click()
    title = wait.until(EC.title_is("Forgot Your Password?"))


@pytest.mark.parametrize("username",["user", "User test", "adm"])
def test_placeholder_username(browser, username):
    """Проверка ввода username"""
    browser.get(browser.url + "/administration/")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="username"]')))
    element.clear()
    element.send_keys(username)
    value_value = element.get_attribute("value")
    assert username == value_value


@pytest.mark.parametrize("password",["123", "qwerty test", "adm"])
def test_placeholder_username(browser, password):
    """Проверка ввода password"""
    browser.get(browser.url + "/administration/")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="password"]')))
    element.clear()
    element.send_keys(password)
    value_value = element.get_attribute("value")
    assert password == value_value


@pytest.mark.parametrize(["username", "password"], [("user", "qwerty"), ("user", "bitnami")])
def test_input_adm(browser, username, password):
    """Проверка авторизации под администратором"""
    browser.get(browser.url + "/administration/")
    wait = WebDriverWait(browser, 1)
    element_username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="username"]')))
    element_username.clear()
    element_username.send_keys(username)
    element_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="password"]')))
    element_password.clear()
    element_password.send_keys(password)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary"]'))).click()
    if username == 'user' and password == 'bitnami':
        title =  wait.until(EC.title_is("Dashboard"))
    else:
        title = wait.until(EC.title_is("Administration"))

