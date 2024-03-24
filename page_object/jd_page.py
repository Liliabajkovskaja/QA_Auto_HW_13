from selenium.webdriver.common.by import By
from page_object.home_page import HomePage


class JDPage(HomePage):
    header_jd_button = "//li[contains(text(), 'Должностные инструкции') or contains(text(), 'JD')]"
    input_name_position = "//input[contains(@class,'filters__input-element')]"
    php_developer_element = "//span[contains(text(), 'PHP разработчик')]"
    input_text = "php"
    sort_up_by_position = "//i[contains(text(), 'keyboard_arrow_up')]"
    sort_down_by_position = "//i[contains(text(), 'keyboard_arrow_down')]"
    last_element_alfabet = "//span[contains(text(), 'Юрист')]"
    first_element_alfabet = "//span[contains(text(), 'Backend разработчик')]"
    table_grid_items = "//div[contains(@class,'table-header__inner table-grid')]/div"
    status_discription_agreed = "(//div[contains(@class,'status-description__text')])[1]"
    status_discription_unagreed = "(//div[contains(@class,'status-description__text')])[2]"
    status_discription_not_filled = "(//div[contains(@class,'status-description__text')])[3]"

    def __init__(self, driver):
        super().__init__(driver)

    def find_table_grid_items(self):
        return self.elements_are_visible((By.XPATH, self.table_grid_items))

    def find_header_dj_button(self):
        return self.element_is_visible((By.XPATH, self.header_jd_button))

    def set_text_into_search_input(self):
        self.fill_input(self.input_text, (By.XPATH, self.input_name_position))
        return self

    def find_php_developer_element(self):
        return self.elements_are_visible((By.XPATH, self.php_developer_element))

    def sort_by_position(self):

        if self.element_is_visible((By.XPATH, self.sort_up_by_position)):
            self.click_button((By.XPATH, self.sort_up_by_position))
        elif self.element_is_visible((By.XPATH, self.sort_down_by_position)):
            self.click_button((By.XPATH, self.sort_down_by_position))
        return self

    def find_sort_up_by_position(self):
        return self.element_is_visible((By.XPATH, self.sort_up_by_position))

    def find_sort_down_by_position(self):
        return self.element_is_visible((By.XPATH, self.sort_down_by_position))

    def find_first_element_alfabet(self):
        return self.element_is_visible((By.XPATH, self.first_element_alfabet))

    def find_last_element_alfabet(self):
        return self.element_is_visible((By.XPATH, self.last_element_alfabet))
