from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPages import MainPage

class MacBookPages(MainPage):
    URL = "/en-gb/product/macbook"
    TITLE = "MacBook"
    H1_MACBOOK = (By.CSS_SELECTOR, 'div[class="col-sm"]>h1')
    IMG_MACBOOK = (By.CSS_SELECTOR, 'img[class="img-thumbnail mb-3"]')
    PATH_MACBOOK = "/image/cache/catalog/demo/macbook_1-500x500.jpg"
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-lg btn-block"]')
    TEXT_BUTTON_CART = (By.CSS_SELECTOR, 'button[class*="btn btn-inverse"]')
    TEXT_COMPARISON = "1 item(s) - $602.00"
    INPUT_QTY = (By.CSS_SELECTOR, 'div[class="mb-3"]>input[class="form-control"]')

    def text_comparing_element(self, element, text):
        wait = WebDriverWait(self.driver, 1)
        wait.until(EC.text_to_be_present_in_element(element, text))

    def input_and_validation(self, element, value_el):
        element.clear()
        element.send_keys(value_el)
        value = element.get_attribute("value")
        return value
