import time
import allure
from page_objects.DesktopsPage import DesktopsPage

@allure.feature("Desktops Page")
def test_title(browser):
    """Проверка заголовка страницы"""
    page = DesktopsPage(browser)
    page.open()
    page.title_site(page.TITLE)

@allure.feature("Desktops Page")
def test_compare(browser):
    """Нажатие на Сравнить твар"""
    page = DesktopsPage(browser)
    page.open()
    page.click_button(page.BUTTON_COMPARE)
    page.title_site(page.TITLE_COMPARE)

@allure.feature("Desktops Page")
def test_sort_by(browser):
    """проверка элемонтов сортировки"""
    page = DesktopsPage(browser)
    page.open()
    elements = page.sech_elements(page.SORT_BY_SELECTOR)
    page.element_comparison(elements, page.SORT_BY)

@allure.feature("Desktops Page")
def test_show(browser):
    """проверка списка Show"""
    page = DesktopsPage(browser)
    page.open()
    elements = page.sech_elements(page.SHOW_SELECTOR)
    page.element_comparison(elements, page.SHOW)

@allure.feature("Desktops Page")
def test_element_components(browser):
    """Проверка появления лементов меню при нажатии на components"""
    page = DesktopsPage(browser)
    page.open()
    elements = page.sech_elements(page.LEFT_MENU)
    select_components = page.seleckt_menu(elements, page.MUNU_COMPONENTS)
    select_components.click()
    time.sleep(2)
    elements_menu_components = page.sech_elements(page.LEFT_MENU)
    element_menu_new = page.element_comparison_list(elements_menu_components, page.ELEMENT_MENU_COMPONENTS)
    assert element_menu_new == page.ELEMENT_MENU_COMPONENTS
