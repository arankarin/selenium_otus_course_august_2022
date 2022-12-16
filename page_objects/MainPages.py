import time
import random
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


    def __init__(self, driver):
        self.driver = driver
        self.main_url = driver.main_url

    def open(self):
        self.driver.get(self.main_url + self.URL)

    def title_site(self, title):
        wait = WebDriverWait(self.driver, 1)
        wait.until(EC.title_is(title))

    def click_button(self, selector):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.presence_of_element_located(selector))
        element.click()

    def main_menu(self):
        names_menu = []
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[class*="navbar"]>li[class*="nav"]')))
        for name in element:
            names_menu.append(name.text)
        return names_menu

    def banner_0_src_foto2(self):
        wait = WebDriverWait(self.driver, 8)
        element = wait.until(EC.element_to_be_clickable(self.IMG_MACBOOKAIR)).get_attribute(
            "src")
        res = True if  int(element.find(self.PATH_MACBOOKAIR)) > 0 else False
        return res

    def element_h1(self, selector):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.visibility_of_element_located(selector))
        return element

    def sech_element_with_element_index(self, element_index, selector):
        wait = WebDriverWait(self.driver, 1)
        elements = wait.until(EC.presence_of_all_elements_located(selector))
        element = elements[element_index]
        title = element.get_attribute("title")
        return element, title

    def sech_element(self, selector):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.presence_of_element_located(selector))
        return element

    def sech_elements(self, selector):
        wait = WebDriverWait(self.driver, 1)
        elements = wait.until(EC.presence_of_all_elements_located(selector))
        return elements

    def button_text_to_cart(self):
        wait = WebDriverWait(self.driver, 1)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button[class*="btn btn-inverse"]'),
                                                    "1 item(s) - $602.00"))

    def fill_input(self, selector, intut_text):
        wait = WebDriverWait(self.driver, 1)
        input_element = wait.until(EC.presence_of_element_located(selector))
        input_element.clear()
        input_element.send_keys(intut_text)

    def search_product(self, text_search):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.presence_of_element_located(self.INPUT_SEARCH))
        element.clear()
        element.send_keys(text_search)
        self.click_button(self.BUTTON_SEARCH)
        try:
            selector = f'//*[text()="{text_search}"]'
            print(f"selector = {selector}")
            return WebDriverWait(self.driver, 1).until(EC.visibility_of_all_elements_located((By.XPATH, selector)))
        except TimeoutException:
            return False

    def generate_random_name(self):
        length = 5
        letters = 'qwjfbfobnwlmefwlpmfwnveofvneweqwc'
        random_name = ''.join(random.choice(letters) for i in range(length))
        return random_name

    def filling_fields_in_product(self):
        product_name = self.generate_random_name()
        meta_tag_title = self.generate_random_name()
        model = self.generate_random_name()
        default = self.generate_random_name()
        new_product = {'product_name': product_name, 'meta_tag_title': meta_tag_title,
                       'model': model, 'default': default}
        return new_product
