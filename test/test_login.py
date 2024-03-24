import pytest


@pytest.mark.smoke
def test_login(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.find_user_name_el()
