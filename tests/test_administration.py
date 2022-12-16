import pytest

from page_objects.AdmPages import AdmPages


def test_title(browser):
    """Проверка заголовка страницы"""
    page = AdmPages(browser)
    page.open()
    page.title_site(page.TITLE)


@pytest.mark.parametrize("username", ["user", "User test", "adm"])
def test_placeholder_username(browser, username):
    """Проверка ввода username"""
    page = AdmPages(browser)
    page.open()
    element = page.sech_element(page.USENAME_SELECTOR)
    element.clear()
    element.send_keys(username)
    value_value = element.get_attribute("value")
    assert username == value_value


@pytest.mark.parametrize("password", ["123", "qwerty test", "adm"])
def test_placeholder_password(browser, password):
    """Проверка ввода password"""
    page = AdmPages(browser)
    page.open()
    element = page.sech_element(page.PASSWORD_SELECTOR)
    element.clear()
    element.send_keys(password)
    value_value = element.get_attribute("value")
    assert password == value_value


@pytest.mark.parametrize(["username", "password"], [("user", "qwerty"), ("user", "bitnami")])
def test_input_adm(browser, username, password):
    """Проверка авторизации под администратором"""
    page = AdmPages(browser)
    page.open()
    page.login_admin(page, username, password)


def test_new_product(browser):
    """Добавление продукта, продукт генерируется случайный"""
    page = AdmPages(browser)
    page.open()
    all_product_fields = page.filling_fields_in_product()
    page.add_product(page, all_product_fields)
    page.driver.get(page.URL_MAIN)
    result = page.search_product(all_product_fields['product_name'])
    assert result


def test_deletproduct(browser):
    """Удаление продукта, сначала добавляем конкретный продукт, потом его удалем"""
    page = AdmPages(browser)
    page.open()
    page.add_product(page, page.PRODUCT_CREATE_YO_DELETE)
    page.menu_products()
    page.fill_input(page.FILTER_PRODUCT_NAME, page.PRODUCT_CREATE_YO_DELETE['product_name'])
    page.click_button(page.BUTTON_FILTER)
    page.element_checkboxe_click()
    page.click_button(page.BUTTON_DELETE)
    browser.switch_to.alert.accept()
    page.driver.get(page.URL_MAIN)
    res = page.search_product(page.PRODUCT_CREATE_YO_DELETE['product_name'])
    assert not res
