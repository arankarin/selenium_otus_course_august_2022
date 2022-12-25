import random
import datetime

import allure
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class MainPage:
    URL = ""
    TITLE = "Your Store"
    MENU = ['Desktops', 'Laptops & Notebooks', 'Components',
            'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'MP3 Players']
    IMG_MACBOOKAIR = ((By.CSS_SELECTOR, 'img[alt="MacBookAir"]'))
    PATH_MACBOOKAIR = "/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg"
    H3_FEATURED = (By.XPATH, '//*[text()="Featured"]')
    IMG_FEATURED = (By.CSS_SELECTOR, 'div[class="image"]>a>img')
    ADD_TO_CART = (By.CSS_SELECTOR, 'div[class="button-group"]>button[title="Add to Cart"]')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'div[class="input-group mb-3"] > button')
    INPUT_SEARCH = (By.CSS_SELECTOR, 'input[class="form-control form-control-lg"]')
    NAME_SEARCH_PRODUCT = (By.XPATH, '//*[text()="Featured"]')
    P_TEXT = (By.CSS_SELECTOR, 'div[id="content"]>p')
    CART_TEXT = "1 item(s) - $602.00"


    def __init__(self, driver):
        self.driver = driver
        self.main_url = driver.main_url
        self.logger = driver.logger


    @allure.step
    def open(self):
        self.logger.info(f"Opening url: {self.main_url}{self.URL}")
        self.driver.get(self.main_url + self.URL)


    @allure.step
    def title_site(self, title):
        self.logger.info(f"Ждем Title: {title}")
        wait = WebDriverWait(self.driver, 1)
        res = wait.until(EC.title_is(title))
        self.logger.debug(f"Получили: {res}")


    @allure.step
    def click_button(self, selector):
        self.logger.info(f"Нажатие на кнопку, Передаем селектор: {selector}")
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.presence_of_element_located(selector))
        element.click()


    @allure.step
    def main_menu(self):
        names_menu = []
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[class*="navbar"]>li[class*="nav"]')))
        for name in element:
            names_menu.append(name.text)
        self.logger.info(f"Элементы главного меню: {names_menu}")
        return names_menu


    @allure.step
    def banner_0_src_foto2(self):
        wait = WebDriverWait(self.driver, 8)
        element = wait.until(EC.element_to_be_clickable(self.IMG_MACBOOKAIR)).get_attribute(
            "src")
        self.logger.info(f"Путь к фото: {element}")
        res = True if int(element.find(self.PATH_MACBOOKAIR)) > 0 else False
        return res


    @allure.step
    def element_h1(self, selector):
        self.logger.info(f"Передаем селектор для h1: {selector}")
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.visibility_of_element_located(selector))
        return element


    @allure.step
    def sech_element_with_element_index(self, element_index, selector):
        wait = WebDriverWait(self.driver, 1)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(selector))
            element = elements[element_index]
            title = element.get_attribute("title")
            self.logger.info(f"Элемент: {element_index}  Подпись фото (значение title): {title}")
            return element, title
        except AssertionError as e:
            self.logger.error(f"Элемент не найден, Ошибка {e}")
            self.driver.save_screenshot(f"logs/sech_element_{datetime.datetime.now()}.png")


    @allure.step
    def sech_element(self, selector):
        self.logger.info(f"Передаем селектор для поиска элемента: {selector}")
        wait = WebDriverWait(self.driver, 1)
        try:
            element = wait.until(EC.presence_of_element_located(selector))
            self.logger.debug("Элемент по селектору найде")
            return element
        except AssertionError as e:
            self.logger.error(f"Элемент не найден, Ошибка {e}")
            self.driver.save_screenshot(f"logs/sech_element_{datetime.datetime.now()}.png")


    @allure.step
    def sech_elements(self, selector):
        self.logger.info(f"Передаем селектор для поиска элементов: {selector}")
        wait = WebDriverWait(self.driver, 1)
        elements = wait.until(EC.presence_of_all_elements_located(selector))
        return elements


    @allure.step
    def button_text_to_cart(self):
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button[class*="btn btn-inverse"]'),
                                                        self.CART_TEXT))
            return True
        except AssertionError as e:
            self.logger.error(f"Текст на кнопке корзины не соответствует {self.CART_TEXT} Ошибка {e}")
            self.driver.save_screenshot(f"logs/button_text_to_cart_{datetime.datetime.now()}.png")


    @allure.step
    def fill_input(self, selector, intut_text):
        self.logger.info(f"Передаем селектор: {selector}")
        self.logger.info(f"Передаем текст для ввода: {intut_text}")
        wait = WebDriverWait(self.driver, 1)
        input_element = wait.until(EC.presence_of_element_located(selector))
        input_element.clear()
        input_element.send_keys(intut_text)
        self.logger.debug("текст введен в поле")


    @allure.step
    def search_product(self, text_search):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.presence_of_element_located(self.INPUT_SEARCH))
        element.clear()
        element.send_keys(text_search)
        self.click_button(self.BUTTON_SEARCH)
        try:
            selector = f'//*[text()="{text_search}"]'
            self.logger.info(f"Селектор для поиска текста на странице {selector}")
            with allure.step(f"Проверка текста на странице, получаем селектор {selector}"):
                return WebDriverWait(self.driver, 1).until(EC.visibility_of_all_elements_located((By.XPATH, selector)))
        except TimeoutException:
            self.driver.save_screenshot(f"logs/search_product_{datetime.datetime.now()}.png")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            return False


    @allure.step
    def generate_random_name(self):
        length = 5
        letters = 'qwjfbfobnwlmefwlpmfwnveofvneweqwc'
        random_name = ''.join(random.choice(letters) for i in range(length))
        return random_name


    @allure.step
    def filling_fields_in_product(self):
        product_name = self.generate_random_name()
        meta_tag_title = self.generate_random_name()
        model = self.generate_random_name()
        default = self.generate_random_name()
        self.logger.info(f"product_name: {product_name}")
        self.logger.info(f"meta_tag_title: {meta_tag_title}")
        self.logger.info(f"model: {model}")
        self.logger.info(f"default: {default}")
        new_product = {'product_name': product_name, 'meta_tag_title': meta_tag_title,
                       'model': model, 'default': default}
        return new_product
