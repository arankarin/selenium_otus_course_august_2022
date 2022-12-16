from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.MainPages import MainPage


class RegisterAccountPages(MainPage):
    URL = "/en-gb?route=account/register"
    TITLE = "Register Account"
    SUBSCRIBE_NO = (By.CSS_SELECTOR, '#input-newsletter-no')
    SUBSCRIBE_YES = (By.CSS_SELECTOR, '#input-newsletter-yes')
    CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    REGISTRATION_NAME_FIELDS = ["firstname", "lastname", "email", "password"]
    BUTTON_CONTINUE = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    INPUT_INVALID = (By.CSS_SELECTOR, 'input[class="form-control is-invalid"]')
    NAME_ATRIBUT = "name"
    ELEMENT_FIRSTNAME = (By.CSS_SELECTOR, 'input[name="firstname"]')
    ELEMENT_ERROR_FIRSTNAME = (By.CSS_SELECTOR, 'div[id="error-firstname"]')
    ELEMENT_ERROR_FIRSTNAME_TEXT = "First Name must be between 1 and 32 characters!"
    ELEMENT_LASTNAME = (By.CSS_SELECTOR, 'input[name="lastname"]')
    ELEMENT_ERROR_LASTNAME = (By.CSS_SELECTOR, 'div[id="error-lastname"]')
    ELEMENT_ERROR_LASTNAME_TEXT = "Last Name must be between 1 and 32 characters!"
    ELEMENT_EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    ELEMENT_ERROR_EMAIL = (By.CSS_SELECTOR, 'div[id="error-email"]')
    ELEMENT_ERROR_EMAIL_TEXT = "E-Mail Address does not appear to be valid!"
    ELEMENT_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    ELEMENT_ERROR_PASSWORD = (By.CSS_SELECTOR, 'div[id="error-password"]')
    ELEMENT_ERROR_PASSWORD_TEXT = "Password must be between 4 and 20 characters!"
    REG_PAGE_TITLE = 'Your Account Has Been Created!'

    def element_select_clickable(self, selector):
        wait = WebDriverWait(self.driver, 1)
        element = wait.until(EC.element_to_be_clickable(selector))
        return element

    def attributes_compare(self, elements, atribut_name_list, atribut_name):
        for name_el in elements:
            assert atribut_name_list.count(name_el.get_attribute(atribut_name))

    def set_value_fields(self):
        first_name = self.generate_random_name()
        last_name = self.generate_random_name()
        em1 = self.generate_random_name()
        em2 = self.generate_random_name()
        email = em1 + '@' + em2 + '.ru'
        password = em1 + em2
        return [first_name, last_name, email, password]

    def register_account(self, page):
        all_value = self.set_value_fields()
        print(all_value)
        page.fill_input(page.ELEMENT_FIRSTNAME, all_value[0])
        page.fill_input(page.ELEMENT_LASTNAME, all_value[1])
        page.fill_input(page.ELEMENT_EMAIL, all_value[2])
        page.fill_input(page.ELEMENT_PASSWORD, all_value[3])
        yes = self.element_select_clickable(self.SUBSCRIBE_YES)
        yes.click()
        print(f".is_selected() = {yes.is_selected()}")
        print(f"element dir = {yes.__dir__()}")
        checkbox = page.element_select_clickable(self.CHECKBOX)
        checkbox.click()
