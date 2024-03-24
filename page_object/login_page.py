import time
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from page_object.home_page import HomePage


class LoginPage(BasePage):
    input_user_name_path = "//input[contains(@ name,'LoginForm[email]')]"
    input_password_path = "// input[contains( @ name, 'LoginForm[password]')]"
    check_box_rememder_me_path = "//i[contains(@class ,'cr-icon icofont icofont-ui-check txt-primary')]"
    button_on_click_login = "// button[contains(@class ,'btn btn-primary btn-md btn-block waves-effect text-center m-b-20')]"
    exit_button = "//div[contains( @class,'navbar-user-exit')]/*/*"
    form_login = "//form[contains(@class,'md-float-material')]"

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_name(self, user_name):
        self.fill_input(user_name, (By.XPATH, self.input_user_name_path))
        return self

    def set_password(self, password):
        self.fill_input(password, (By.XPATH, self.input_password_path))
        return self

    def click_login(self):
        self.click_button((By.XPATH, self.button_on_click_login))
        return HomePage(self.driver)

    def do_login(self, user_name, password):
        self.set_user_name(user_name)
        self.set_password(password)
        self.click_login()
        return self

    def do_log_out(self):
        self.click_button((By.XPATH, self.exit_button))
        return self
