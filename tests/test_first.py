
def test_hello_selenium(driver):
    driver.get(url="https://www.opencart.com/")
    assert driver.title == "OpenCart - OpenSource Shopping Cart Solution"


def test_hello_selenium2(driver):
    driver.get(url="https://www.opencart.com/")
    # driver.save_screenshot("test.png")
    assert driver.title == "OpenCart - Open Source Shopping Cart Solution"
