import pytest

from page_objects.MacBookPages import MacBookPages


def test_title(browser):
    """Проверка заголовка страницы"""
    page = MacBookPages(browser)
    page.open()
    page.title_site(page.TITLE)


def test_h1_acbook(browser):
    """Проверка названия товара"""
    page = MacBookPages(browser)
    page.open()
    h1 = page.element_h1(page.H1_MACBOOK)
    assert h1.text == page.TITLE


def test_img_macbook(browser):
    """Проверка отобрадаеися картинки макбука"""
    page = MacBookPages(browser)
    page.open()
    img = page.sech_element(page.IMG_MACBOOK).get_attribute("src")
    res = True if int(img.find(page.PATH_MACBOOK)) > 0 else False


def test_button_add_to_cart(browser):
    """Проверка кнопки добавления в корзину"""
    page = MacBookPages(browser)
    page.open()
    page.click_button(page.BUTTON_ADD_TO_CART)
    page.text_comparing_element(page.TEXT_BUTTON_CART, page.TEXT_COMPARISON)


@pytest.mark.parametrize("value_el", ["2", "4", "22"])
def test_quantity(browser, value_el):
    """Проверка вводимого текста в элемент"""
    page = MacBookPages(browser)
    page.open()
    element = page.sech_element(page.INPUT_QTY)
    value = page.input_and_validation(element, value_el)
    assert value_el == value
