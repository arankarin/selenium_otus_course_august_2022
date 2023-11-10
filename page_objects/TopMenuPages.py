import allure

from selenium.webdriver.common.by import By

from page_objects.MainPages import MainPage


class TopMenuPages(MainPage):
    PATH = ""
    CURRENCY = (By.CSS_SELECTOR, 'strong')
    EUR = (By.CSS_SELECTOR, 'a[href="EUR"]')
    POUND_STERLING = (By.CSS_SELECTOR, 'a[href="GBP"]')
    USD = (By.CSS_SELECTOR, 'a[href="USD"]')

    @allure.step
    def currency_click(self, selector):
        elements = self.sech_element(selector)
        elements.click()
        self.logger.info(f"Передаем селектор {selector} и нажимаем")
