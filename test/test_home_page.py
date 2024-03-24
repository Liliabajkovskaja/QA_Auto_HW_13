import time
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_title_news_are_unique(get_logged_home_page):
    home_page = get_logged_home_page
    titles = home_page.get_news_titles_text()
    assert len(titles) == len(set(titles)), "You have non-unique elements"


@pytest.mark.regression
def test_change_language(get_logged_home_page):
    home_page = get_logged_home_page
    button_language_locator = home_page.button_languge
    change_to_language_locator = home_page.change_to_en
    el = home_page.change_language(button_language_locator, change_to_language_locator)
    el.find_header_home_button()


@pytest.mark.regression
def test_menu_elements_count(get_logged_home_page):
    home_page = get_logged_home_page
    menu_elements = home_page.find_menu_els()
    assert len(menu_elements) == 14
    f"Expected 14 menu elements, but found {len(menu_elements)}"


@pytest.mark.regression
def test_scroll_to_6_element(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.scroll_by_selenium_to_last_item(6)
    time.sleep(2)


@pytest.mark.regression
def test_go_to_user_notification(get_logged_home_page):
    home_page = get_logged_home_page
    home_page.find_user_notification()
