from selenium.webdriver.common.by import By
from page_object.home_page import HomePage


class Reports_ProcesPage(HomePage):

    def __init__(self, driver):
        super().__init__(driver)

    header_reports_proces_button = "//li[contains(@class,'active')]"
    reports_blocks = "//div[contains(@class,'row reports_blocks')]/div"
    plan_fact_analys = "//div[contains(@class,'row reports_blocks')]/div[1]"
    fact_import = "//div[contains(@class,'row reports_blocks')]/div[2]"
    plan_import = "//div[contains(@class,'row reports_blocks')]/div[3]"
    reports_settings_title = "//div[contains(@class,'reports_settings_title')]"
    button_import_actual_from_excel = "//input[contains(@class,'btn btn-success')]"
    select_department = "//select[contains(@class,'form-control')]"

    def find_header_reports_proces_button(self):
        return self.element_is_visible((By.XPATH, self.header_reports_proces_button))

    def find_reports_settings_title(self):
        return self.element_is_visible((By.XPATH, self.reports_settings_title))

    def find_button_import_actual_from_excel(self):
        return self.element_is_visible((By.XPATH, self.button_import_actual_from_excel))

    def find_select_department(self):
        return self.element_is_visible((By.XPATH, self.select_department))

    def find_reports_blocks(self):
        return self.elements_are_visible((By.XPATH, self.reports_blocks))

    def find_plan_fact_analys(self):
        return self.element_is_clickable((By.XPATH, self.plan_fact_analys))

    def find_fact_import(self):
        return self.element_is_clickable((By.XPATH, self.fact_import))

    def find_plan_import(self):
        return self.element_is_clickable((By.XPATH, self.plan_import))

    def go_to_plan_fact_analis(self):
        self.click_button((By.XPATH, self.plan_fact_analys))
        return self

    def go_to_fact_import(self):
        self.click_button((By.XPATH, self.fact_import))
        return self

    def go_to_plan_import(self):
        self.click_button((By.XPATH, self.plan_import))
        return self
