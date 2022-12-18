import time
import allure

from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPages import MainPage


class AdmPages(MainPage):
    URL = "/administration/"
    TITLE = "Administration"
    USENAME_SELECTOR = (By.XPATH, '//*[@name="username"]')
    PASSWORD_SELECTOR = (By.XPATH, '//*[@name="password"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    USENAME = "user"
    PASSWORD = "bitnami"
    PRODUCT_CREATE_YO_DELETE = {'product_name': 'Name001', 'meta_tag_title': 'test meta tag title',
                                'model': 'test model', 'default': 'test default'}
    MENU_CATALOG = ((By.CSS_SELECTOR, '#menu-catalog'))
    MENU_PRODUCT = (By.XPATH, '//a[text()="Products"]')
    MENU_PRODUCT_CSS = (By.CSS_SELECTOR, 'ul[id="collapse-1"]>li')
    BUTTON_ADD_NEW_PRODUCT = (By.CSS_SELECTOR, 'div[class="float-end"]>a')
    GENERAL_PRODUKT_NAME = (By.CSS_SELECTOR, 'input[placeholder="Product Name"]')
    GENERAL_META_TAG_TITLE = (By.CSS_SELECTOR, 'input[placeholder="Meta Tag Title"]')
    MENU_DATA = (By.CSS_SELECTOR, '.nav.nav-tabs li:nth-child(2) a')
    DATA_MODEL = ((By.CSS_SELECTOR, 'input[placeholder="Model"]'))
    MENU_SEO = (By.CSS_SELECTOR, '.nav.nav-tabs li:nth-child(11) a')
    SEO_DEFAULT = (By.CSS_SELECTOR, 'input[placeholder="Keyword"]')
    BUTTON_SAVE_PRODUCT = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    URL_MAIN = "http://172.16.16.20:8081/"
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, 'input[placeholder="Product Name"]')
    BUTTON_FILTER = (By.CSS_SELECTOR, 'button[id="button-filter"]')
    CHECKBOX = (By.CSS_SELECTOR, 'input[name="selected[]"]')
    BUTTON_DELETE = (By.CSS_SELECTOR, 'button[title="Delete"]')

    @allure.step
    def login_admin(self, page, username='', password=''):
        self.logger.info(f"Передаем page: {page}")
        self.logger.info(f"Передаем username: {username}")
        self.logger.info(f"Передаем password: {password}")
        wait = WebDriverWait(self.driver, 1)
        el_username = page.sech_element(page.USENAME_SELECTOR)
        el_username.clear()
        el_username.send_keys(username)
        el_password = page.sech_element(page.PASSWORD_SELECTOR)
        el_password.clear()
        el_password.send_keys(password)
        page.click_button(page.BUTTON_LOGIN)
        if username == 'user' and password == 'bitnami':
            page.title_site("Dashboard")
            self.logger.info(f"Вход под администратором осуществлен")
            return page
        else:
            self.logger.info(f"Вход НЕ осуществлен, остались на странице входа")
            page.title_site("Administration")

    @allure.step
    def menu_products(self):
        wait = WebDriverWait(self.driver, 1)
        all_nemu_nav_tabs = wait.until(
            EC.presence_of_all_elements_located(self.MENU_PRODUCT_CSS))
        menu_nav_tabs = all_nemu_nav_tabs[1]
        self.logger.info(f"Выбрано меню по селектору: {self.MENU_PRODUCT_CSS}")
        time.sleep(2)  # Обязательная пауза
        menu_nav_tabs.click()
        self.logger.debug("Нажата кнопка меню")
        return menu_nav_tabs

    @allure.step
    def add_product(self, page, new_product):
        self.logger.info(f"new_product: {new_product}")
        page.login_admin(page, page.USENAME, page.PASSWORD)
        page.sech_element(page.MENU_CATALOG).click()
        page.menu_products()
        page.click_button(page.BUTTON_ADD_NEW_PRODUCT)
        page.fill_input(self.GENERAL_PRODUKT_NAME, new_product['product_name'])
        page.fill_input(self.GENERAL_META_TAG_TITLE, new_product['meta_tag_title'])
        data_menu = page.sech_element(self.MENU_DATA)
        data_menu.click()
        page.fill_input(self.DATA_MODEL, new_product['model'])
        seo_menu = page.sech_element(self.MENU_SEO)
        seo_menu.click()
        page.fill_input(self.SEO_DEFAULT, new_product['default'])
        page.click_button(self.BUTTON_SAVE_PRODUCT)

    @allure.step
    def fill_input_1(self, selector, intut_text):
        wait = WebDriverWait(self.driver, 1)
        input_element = wait.until(EC.presence_of_element_located(selector))
        input_element.clear()
        input_element.send_keys(intut_text)

    @allure.step
    def element_checkboxe_click(self, selector):
        self.logger.info(f"Передаем селектор для checkboxe: {selector}")
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.visibility_of_element_located(selector))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()
