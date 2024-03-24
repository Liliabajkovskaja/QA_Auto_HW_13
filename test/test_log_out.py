import time
import pytest
from page_object.log_out_page import LogoutPage


@pytest.mark.smoke
def test_logout(get_logged_home_page):
    home_page = get_logged_home_page
    logout_page = LogoutPage(home_page.driver)
    time.sleep(1)
    logout_page.do_log_out()
