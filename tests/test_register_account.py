import time
import allure

from page_objects.RegisterAccountPages import RegisterAccountPages

@allure.feature("Register Account Page")
def test_title(browser):
    """Проверка заголовка страницы"""

    page = RegisterAccountPages(browser)
    page.open()
    page.title_site(page.TITLE)

@allure.feature("Register Account Page")
def test_subscribe_radio(browser):
    """Проверка Subscribe выбрано по умолчанию No"""
    page = RegisterAccountPages(browser)
    page.open()
    element = page.element_select_clickable(page.SUBSCRIBE_NO)
    print(f"print dir = {print.__dir__()}")
    assert element.is_selected()

@allure.feature("Register Account Page")
def test_checkbox(browser):
    """Проверка по умолчанию checkbox галочка не стоит, при нажатии галочка ставится"""
    page = RegisterAccountPages(browser)
    page.open()
    element = page.element_select_clickable(page.CHECKBOX)
    assert not element.is_selected()
    element.click()
    assert element.is_selected()

@allure.feature("Register Account Page")
def test_continue_empty_fields(browser):
    """проверть кнопку continue с пустыми полями  становится красным"""
    page = RegisterAccountPages(browser)
    page.open()
    button = page.sech_element(page.BUTTON_CONTINUE)
    button.click()
    elements = page.sech_elements(page.INPUT_INVALID)
    page.attributes_compare(elements, page.REGISTRATION_NAME_FIELDS, page.NAME_ATRIBUT)

@allure.feature("Register Account Page")
def test_continue_invalid_fields(browser):
    """проверть кнопку continue с пустыми полями появляется подпись под полями"""
    page = RegisterAccountPages(browser)
    page.open()
    button = page.sech_element(page.BUTTON_CONTINUE)
    button.click()
    element_error_firstname = page.sech_element(page.ELEMENT_ERROR_FIRSTNAME)
    assert element_error_firstname.text == page.ELEMENT_ERROR_FIRSTNAME_TEXT

    element_error_lastname = page.sech_element(page.ELEMENT_ERROR_LASTNAME)
    assert element_error_lastname.text == page.ELEMENT_ERROR_LASTNAME_TEXT

    element_error_emaile = page.sech_element(page.ELEMENT_ERROR_EMAIL)
    assert element_error_emaile.text == page.ELEMENT_ERROR_EMAIL_TEXT

    element_error_password = page.sech_element(page.ELEMENT_ERROR_PASSWORD)
    assert element_error_password.text == page.ELEMENT_ERROR_PASSWORD_TEXT

@allure.feature("Register Account Page")
def test_register_account(browser):
    """Регистрация нового пользователя"""
    page = RegisterAccountPages(browser)
    page.open()
    page.register_account(page)
    button = page.click_button(page.BUTTON_CONTINUE)
    page.title_site(page.REG_PAGE_TITLE)
    time.sleep(2)
