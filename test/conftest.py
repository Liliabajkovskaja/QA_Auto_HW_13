from pytest import fixture
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.blue_red_books_page import BlueRedBooksPage
from page_object.jd_page import JDPage
from page_object.login_page import LoginPage
from page_object.home_page import HomePage
from page_object.reports_proces_page import Reports_ProcesPage
from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory


@fixture(scope='session')
def get_driver() -> WebDriver:
    driver = DriverFactory(ConfigManager.browser).get_driver()
    yield driver
    driver.quit()


@fixture
def open_login_page(get_driver) -> WebDriver:
    get_driver.get(ConfigManager.url)
    return get_driver


@fixture(scope='session')
def get_user_name() -> str:
    return ConfigManager.user_name


@fixture(scope='session')
def get_password() -> str:
    return ConfigManager.user_pass


@fixture
def get_logged_home_page(open_login_page, get_user_name, get_password) -> HomePage:
    try:
        return HomePage(open_login_page).find_user_name_el()
    except TimeoutException:
        LoginPage(open_login_page).do_login(get_user_name, get_password)
        return HomePage(open_login_page)


@fixture
def go_to_blue_red_books_page(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.go_to_blue_red_books_page()
    return BlueRedBooksPage(home_page.driver)


@fixture
def go_to_jd_page(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.go_to_jd_page()
    return JDPage(home_page.driver)


@fixture
def go_to_reports_proces_page(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.go_to_reports_proces_page()
    return Reports_ProcesPage(home_page.driver)
