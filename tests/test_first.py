import allure
import pytest

from page_objects.MainPages import MainPage
from page_objects.SearchPages import SearchPages
from page_objects.TopMenuPages import TopMenuPages

@allure.feature("Main Pages")
@allure.title('Title check "Your Store"')
def test_title(browser):
    """Проверка заголовка страницы"""
    page = MainPage(browser)
    page.open()
    page.title_site(page.TITLE)

@allure.feature("Main Pages")
def test_button_search(browser):
    """Проверка переходна на страницу поиска после нажария на кнопку поиска"""
    page = MainPage(browser)
    page.open()
    page.click_button(page.BUTTON_SEARCH)
    page.title_site(SearchPages.TITLE)

@allure.feature("Main Pages")
def test_main_menu(browser):
    """Проверка названий основного меню"""
    page = MainPage(browser)
    page.open()
    menu = page.main_menu()
    assert page.MENU == menu

@allure.feature("Main Pages")
def test_banner_0_src_foto2(browser):
    """Ожидание появления на странице MacBookAir и проверука пути до фото"""
    page = MainPage(browser)
    page.open()
    banner = page.banner_0_src_foto2()
    assert banner

@allure.feature("Main Pages")
def test_element_h1(browser):
    """Проверка наличия заголовка h3 с текстом Featured"""
    page = MainPage(browser)
    page.open()
    page.element_h1(page.H3_FEATURED)

@allure.feature("Main Pages")
@pytest.mark.xfail(reason="Дефект на элементе 2, 'Apple Cinema 30\"' != 'Apple Cinema 30' Дефект на элементе 3 'Canon EOS 5D' != 'sdf'")
@pytest.mark.parametrize("element_index", [0, 1, 2, 3])
def test_amount_product_thumb(browser, element_index):
    """Проверка сответствия, ссылка из блока Featured ведет на страницу с заголовком товара"""
    page = MainPage(browser)
    page.open()
    elament, title_element = page.sech_element_with_element_index(element_index, page.IMG_FEATURED)
    elament.click()
    page.title_site(title_element)


def test_button_group_Add_to_Cart(browser):
    """Проверка отображения добавленного товара на кнопке корзина"""
    page = MainPage(browser)
    page.open()
    element, title_element = page.sech_element_with_element_index(0, page.ADD_TO_CART)
    element.click()
    assert page.button_text_to_cart()


def test_top_menu_currency(browser):
    """Проверка переключения валюты"""
    page = TopMenuPages(browser)
    page.open()
    assert page.sech_element(page.CURRENCY).text == '$'
    page.currency_click(page.CURRENCY)
    pound_sterling = page.sech_element(page.POUND_STERLING)
    pound_sterling.click()
    assert page.sech_element(page.CURRENCY).text == '£'
    page.currency_click(page.CURRENCY)
    usd = page.sech_element(page.USD)
    usd.click()
    assert page.sech_element(page.CURRENCY).text == '$'
