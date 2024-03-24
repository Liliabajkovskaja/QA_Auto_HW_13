import time
from selenium.webdriver.common.by import By
from page_object.home_page import HomePage


class BlueRedBooksPage(HomePage):
    header_menu_element = "//li[contains(@class,'active')]"
    add_income_button = "(//div[contains(@class,'p-t-10 p-b-10 text-uppercase b-r-table-value-title n-table-left b-r-table-value-title')]//span)[1]"
    add_cost_button = "(//div[contains(@class,'p-t-10 p-b-10 text-uppercase b-r-table-value-title n-table-left b-r-table-value-title')]//span)[2]"
    basic_income_article = "//li[contains(text(), 'Базовые статьи')]"
    cost_trademarks = "//li[contains(text(), 'Товарные знаки')]"
    main_department_button = "//div[contains(@class,'imp-brcrumbs__inner-btns')]"
    all_structure = "//div[contains(@class,'org-tree__data')]"
    structure_dep_lev_1 = "(//div[contains(@class,'org-tree__name')])[1]"
    structure_dep_lev_2 = "(//div[contains(@class,'org-tree__name')])[2]"
    structure_dep_lev_3 = "(//div[contains(@class,'org-tree__name')])[3]"

    def __init__(self, driver):
        super().__init__(driver)

    def find_structure_dep_lev_1(self):
        return self.elements_are_visible((By.XPATH, self.structure_dep_lev_1))

    def find_all_structure(self):
        return self.elements_are_visible((By.XPATH, self.all_structure))

    def find_main_department_button(self):
        return self.element_is_clickable((By.XPATH, self.main_department_button))

    def open_structure_department(self):
        self.click_button((By.XPATH, self.main_department_button))
        return self

    def find_header_menu_element(self):
        return self.elements_are_visible((By.XPATH, self.header_menu_element))

    def click_add_income_button(self):
        self.click_button((By.XPATH, self.add_income_button))
        return self

    def find_basic_articles(self):
        self.element_is_visible((By.XPATH, self.basic_income_article))
        return self

    def click_add_cost_button(self):
        self.click_button((By.XPATH, self.add_cost_button))
        return self

    def find_costs_cost_trademarks(self):
        self.element_is_visible((By.XPATH, self.cost_trademarks))
        return self
