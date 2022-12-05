import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_title(browser):
    """Проверка заголовка страницы"""
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.title_is("Your Store"))


def test_button_search(browser):
    """Проверка переходна на страницу поиска после нажария на кнопку поиска"""
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="input-group mb-3"] > button')))
    element.click()
    browser_title = browser.title
    assert browser_title == "Search"


def test_main_menu(browser):
    """Проверка названий основного меню"""
    menu = ['Desktops', 'Laptops & Notebooks', 'Components',
            'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'MP3 Players']
    names_menu = []
    wait = WebDriverWait(browser, 1)
    element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[class*="navbar"]>li[class*="nav"]')))
    for name in element:
        names_menu.append(name.text)
    # res = browser.find_elements(By.CSS_SELECTOR, 'ul[class*="navbar"]>li[class*="nav"]')
    assert menu == names_menu


def test_banner_0_src_foto2(browser):
    """Ожидание появления на странице MacBookAir и проверука пути до фото"""
    wait = WebDriverWait(browser, 8)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="MacBookAir"]'))).get_attribute("src")
    assert int(element.find("/image/cache/catalog/demo/banners/MacBookAir-1140x380.jpg")) > 0

def test_element_h1(browser):
    """Проверка наличия заголовка h3 с текстом Featured"""
    element = browser.find_elements(By.XPATH, '//*[text()="Featured"]')


#Дефект на элементе 2, 'Apple Cinema 30"' != 'Apple Cinema 30'
#Дефект на элементе 3 'Canon EOS 5D' != 'sdf'
@pytest.mark.parametrize("element_index", [0, 1])
def test_amount_product_thumb(browser, element_index):
    """Проверка сответствия, ссылка из блока Featured ведет на страницу с заголовком товара"""
    elements = browser.find_elements(By.CSS_SELECTOR, 'div[class="image"]>a>img')
    assert len(elements) == 4
    elements_titles = elements[element_index].get_attribute("title")
    elements[element_index].click()
    browser_title = browser.title
    assert elements_titles == browser_title


def test_button_group_Add_to_Cart(browser):
    """Проверка отображения добавленного товара на кнопке корзина"""
    wait =WebDriverWait(browser, 1)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="button-group"]>button[title="Add to Cart"]')))
    elements[0].click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button[class*="btn btn-inverse"]'), "1 item(s) - $602.00"))


