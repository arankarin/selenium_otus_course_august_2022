import allure

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

    @allure.step
    def element_comparison(self, elements, element_sort):
        self.logger.info(f"Элементы для проверки: {element_sort}")
        for selected_options in elements:
            self.logger.info(f"Элементы в списке: {selected_options.text}")
            res = element_sort.count(selected_options.text)
            assert res == 1

    @allure.step
    def seleckt_menu(self, elements, name_menu):
        self.logger.info(f"Название меню, которое ищем: {name_menu}")
        res = -1
        for list_group_item in elements:
            res = list_group_item.text.find(name_menu)
            if res == 0:
                component = list_group_item
                self.logger.debug(f"меню есть: {name_menu}")
                return component
        if res == -1:
            self.logger.error("переданное название не нашлось в меню")

    @allure.step
    def element_comparison_list(self, elements, element_menu):
        self.logger.info(f"Элементы для сравнения: {element_menu}")
        element_menu_new = []
        for el in element_menu:
            for i in elements:
                i_text = i.text
                if i_text.count(el) > 0:
                    element_menu_new.append(el)
        self.logger.info(f"Названия меню, которые получили: {element_menu_new}")
        return element_menu_new
