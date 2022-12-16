from selenium.webdriver.common.by import By

from page_objects.MainPages import MainPage


class DesktopsPage(MainPage):
    URL = "/en-gb/catalog/desktops/"
    TITLE = "Desktops"
    BUTTON_COMPARE = (By.CSS_SELECTOR, 'div[class="mb-3"] > a')
    TITLE_COMPARE = 'Product Comparison'
    SORT_BY = ["Default", "Name (A - Z)", "Name (Z - A)", "Price (Low > High)", "Price (High > Low)",
               "Rating (Highest)", "Rating (Lowest)", "Model (A - Z)", "Model (Z - A)"]
    SORT_BY_SELECTOR = (By.CSS_SELECTOR, '#input-sort > option')
    SHOW_SELECTOR = (By.CSS_SELECTOR, '#input-limit > option')
    SHOW = ["10", "25", "50", "75", "100"]
    ELEMENT_MENU_COMPONENTS = ["Mice and Trackballs", "Monitors", "Printers", "Scanners", "Web Cameras"]
    LEFT_MENU = (By.CSS_SELECTOR, 'a[class="list-group-item"]')
    MUNU_COMPONENTS = "Components"

    def element_comparison(self, elements, element_sort):
        for selected_options in elements:
            res = element_sort.count(selected_options.text)
            assert res == 1

    def seleckt_menu(self, elements, name_menu):
        for list_group_item in elements:
            res = list_group_item.text.find(name_menu)
            if res == 0:
                component = list_group_item
                return component

    def element_comparison_list(self, elements, element_menu):
        element_menu_new = []
        for el in element_menu:
            for i in elements:
                i_text = i.text
                if i_text.count(el) > 0:
                    element_menu_new.append(el)
        return element_menu_new
