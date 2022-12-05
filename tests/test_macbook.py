import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    """Проверка заголовка страницы"""
    browser.get(browser.url + "/en-gb/product/macbook")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.title_is("MacBook"))


def test_h1_acbook(browser):
    """Проверка названия товара"""
    browser.get(browser.url + "/en-gb/product/macbook")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
    assert element.text == "MacBook"


def test_img_macbook(browser):
    """Проверка отобрадаеися картинки макбука"""
    browser.get(browser.url + "/en-gb/product/macbook")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[class="img-thumbnail mb-3"]'))).get_attribute("src")
    assert int(element.find("/image/cache/catalog/demo/macbook_1-500x500.jpg")) > 0


def test_button_add_to_cart(browser):
    """Проверка кнопки добавления в корзину"""
    browser.get(browser.url + "/en-gb/product/macbook")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn btn-primary btn-lg btn-block"]')))
    element.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button[class*="btn btn-inverse"]'), "1 item(s) - $602.00"))


@pytest.mark.parametrize("value_el", ["2", "4", "22"])
def test_quantity(browser, value_el):
    """Проверка вводимого текста в элемент"""
    browser.get(browser.url + "/en-gb/product/macbook")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="mb-3"]>input[class="form-control"]')))
    element.clear()
    element.send_keys(value_el)
    value = element.get_attribute("value")
    assert value_el == value






