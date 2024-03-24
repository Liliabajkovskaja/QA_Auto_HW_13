import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HomePage(BasePage):
    user_name_el_path = "//h5[contains(@class,'navbar-top-username')]"
    news_titles = "//div[contains(@class,'news_container notread')]//b"
    button_languge = "//div[contains(@role,'button')]"
    change_to_en = "(//div[contains(@class,'v-list-item theme--light')])[2]"
    change_to_ru = "(//div[contains(@class,'v-list-item theme--light')])[1]"
    header_home_button = "//ul[contains(@class,'breadcrumb')]//a"
    menu_elements = "//div[contains(@class,'navbar-menu-item-container')]"
    user_notification = "//div[contains(@class,'navbar-user-notifications')]"
    menu_black_books = "(//div[contains(@class,'navbar-menu-item-container')])[2]"
    menu_change = "(//div[contains(@class,'navbar-menu-item-container')])[3]"
    menu_dj = "(//div[contains(@class,'navbar-menu-item-container')])[4]"
    menu_blue_red_books = "(//div[contains(@class,'navbar-menu-item-container')])[5]"
    menu_office_and_responsible = "(//div[contains(@class,'navbar-menu-item-container')])[6]"
    menu_projects = "(//div[contains(@class,'navbar-menu-item-container')])[7]"
    menu_catalogues = "(//div[contains(@class,'navbar-menu-item-container')])[8]"
    menu_glossary = "(//div[contains(@class,'navbar-menu-item-container')])[9]"
    menu_news = "(//div[contains(@class,'navbar-menu-item-container')])[10]"
    menu_reports_and_processing = "(//div[contains(@class,'navbar-menu-item-container')])[11]"
    menu_dashboards = "(//div[contains(@class,'navbar-menu-item-container')])[12]"
    menu_reverse_structure = "(//div[contains(@class,'navbar-menu-item-container')])[13]"
    menu_administation = "(//div[contains(@class,'navbar-menu-item-container')])[14]"
    news_items = "//div[contains(@class,'news_article')]"
    last_new = "(//div[contains(@class,'news_article')])[last()]"
    button_add_new = "//div[contains(@class,'add_button btn-group f-right')]"
    form_add_new = "//body[contains(@class,'cke_editable cke_editable_themed cke_contents_ltr cke_show_borders')]"
    button_save_new = "//button[contains(@class,'btn btn-success')]"
    notification_content = "//div[contains(@class,'notifications-content')]"
    come_main_page_button = "//div[contains(@class,'navbar-logo')]"

    def __init__(self, driver):
        super().__init__(driver)

    def find_user_name_el(self):
        self.element_is_visible((By.XPATH, self.menu_elements))
        return self

    def find_menu_els(self):
        return self.elements_are_visible((By.XPATH, self.menu_elements))

    def find_header_home_button(self):
        self.element_is_visible((By.XPATH, self.header_home_button))
        return self

    def go_to_blue_red_books_page(self):
        self.click_button((By.XPATH, self.menu_blue_red_books))

    def go_to_jd_page(self):
        self.click_button((By.XPATH, self.menu_dj))

    def go_to_reports_proces_page(self):
        self.click_button((By.XPATH, self.menu_reports_and_processing))

    def get_news_titles_text(self) -> list[str]:
        return self.get_texts(locator=(By.XPATH, self.news_titles))

    def get_language(self, locator_language):
        if locator_language == self.change_to_en:
            return self.change_to_en
        elif locator_language == self.change_to_ru:
            return self.change_to_ru

    def change_language(self, button_language_locator, change_to_language_locator):
        self.click_button(locator=(By.XPATH, button_language_locator))
        self.click_button((By.XPATH, change_to_language_locator))
        return self

    def scroll_by_selenium_to_last_item(self, number):
        el = self.get_element_by_number(locator=(By.XPATH, self.news_items), number=number)
        ActionChains(driver=self.driver).scroll_to_element(el).perform()

    def go_to_user_notification(self):
        self.click_button(locator=(By.XPATH, self.user_notification))
        return self

    def find_user_notification(self):
        self.go_to_user_notification()
        self.click_button((By.XPATH, self.notification_content))
        return self

    def come_back_to_main_page(self):
        self.click_button((By.XPATH, self.come_main_page_button))
