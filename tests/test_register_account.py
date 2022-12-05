import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    """Проверка заголовка страницы"""
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.title_is("Register Account"))


def test_subscribe_radio(browser):
    """Проверка Subscribe выбрано по умолчанию No"""
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-newsletter-no'))).is_selected()
    assert element


def test_checkbox(browser):
    """Проверка по умолчанию checkbox галочка не стоит, при нажатии галочка ставится"""
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="checkbox"]')))
    element_selected = element.is_selected()
    assert not element_selected
    element.click()
    element_selected = element.is_selected()
    assert element_selected


def test_continue_empty_fields(browser):
    """проверть кнопку continue с пустыми полями  становится красным"""
    name = ["firstname", "lastname", "email", "password"]
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary"]'))).click()
    element_new = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[class="form-control is-invalid"]')))
    for name_el in element_new:
        assert name.count(name_el.get_attribute("name"))


def test_continue_invalid_fields(browser):
    """проверть кнопку continue с пустыми полями появляется подпись под полями"""
    name = ["firstname", "lastname", "email", "password"]
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary"]'))).click()
    element_error_firstname = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id="error-firstname"]')))
    element_error_lastname = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id="error-lastname"]')))
    element_error_emaile = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id="error-email"]')))
    element_error_password = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id="error-password"]')))
    assert element_error_firstname[0].text == "First Name must be between 1 and 32 characters!"
    assert element_error_lastname[0].text == "Last Name must be between 1 and 32 characters!"
    assert element_error_emaile[0].text == "E-Mail Address does not appear to be valid!"
    assert element_error_password[0].text == "Password must be between 4 and 20 characters!"


@pytest.mark.skip(reason="Выполняется 1 раз, т.к. происходит регистрация и пользователь есть в базе.")
def test_continue_true(browser):
    """Проврка регистрации пользователя"""
    browser.get(browser.url + "/en-gb?route=account/register")
    wait = WebDriverWait(browser, 1)
    first_name = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="input-firstname"]'))).send_keys("qwerty")
    last_name = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="input-lastname"]'))).send_keys("fqwerty")
    email = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="input-email"]'))).send_keys("qw@qw.qw")
    password = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="input-password"]'))).send_keys("password")
    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="checkbox"]'))).click()
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary"]'))).click()
    element = wait.until(EC.title_is("Your Account Has Been Created!"))







