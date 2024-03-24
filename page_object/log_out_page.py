from selenium.webdriver.common.by import By
from page_object.base_page import BasePage



class LogoutPage(BasePage):
    exit_button = "//div[contains( @class,'navbar-user-exit')]/*/*"
    form_login = "//form[contains(@class,'md-float-material')]"

    def __init__(self, driver):
        super().__init__(driver)

    def do_log_out(self):
        self.click_button((By.XPATH, self.exit_button))
        return self

    def find_login_form(self):
        self.element_is_visible((By.XPATH, self.form_login))
        return self
