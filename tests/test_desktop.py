import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    """Проверка заголовка страницы"""
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.title_is("Desktops"))

def test_compare(browser):
    """Нажатие на Сравнить твар"""
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="mb-3"] > a')))
    element.click()
    browser_title = browser.title
    assert browser_title == "Product Comparison"


def test_sort_by(browser):
    """проверка элемонтов сортировки"""
    options = ["Default", "Name (A - Z)", "Name (Z - A)", "Price (Low > High)", "Price (High > Low)", "Rating (Highest)", "Rating (Lowest)", "Model (A - Z)", "Model (Z - A)"]
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 1)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#input-sort > option')))
    for selected_options in elements:
        res = options.count(selected_options.text)
        assert res == 1


def test_show(browser):
    """проверка списка Show"""
    options = ["10", "25", "50", "75", "100"]
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 1)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#input-limit > option')))
    for selected_options in elements:
        res = options.count(selected_options.text)
        assert res == 1


def test_element_components(browser):
    """Проверка появления лементов меню при нажатии на components"""
    browser.get(browser.url + "/en-gb/catalog/desktops")
    element_menu = ["Mice and Trackballs", "Monitors", "Printers", "Scanners", "Web Cameras"]
    element_menu_new = []
    wait = WebDriverWait(browser, 1)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="list-group-item"]')))
    for list_group_item in elements:
        res = list_group_item.text.find("Components")
        if res == 0:
            components = list_group_item
            components.click()
            elements_menu_components = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="list-group-item"]')))
            for el in element_menu:
                for i in elements_menu_components:
                    i_text = i.text
                    if i_text.count(el) > 0:
                        element_menu_new.append(el)
            break
    assert element_menu == element_menu_new

