import time
import pytest
from page_object.news_page import NewsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_read_news(get_logged_home_page):
    home_page = get_logged_home_page
    news_page = NewsPage(home_page.driver)
    news_text = news_page.read_news(1).get_text_from_news()
    assert news_text, "News don`t exist text"


@pytest.mark.regression
def test_find_news_titles(get_logged_home_page):
    home_page = get_logged_home_page
    news_page = NewsPage(home_page.driver)
    news_page.read_news(1).find_news_titles()


@pytest.mark.regression
def test_find_count_people_viewed(get_logged_home_page):
    home_page = get_logged_home_page
    news_page = NewsPage(home_page.driver)
    news_page.read_news(1).find_count_people_viewed()


@pytest.mark.regression
def test_find_button_prev_page_news(get_logged_home_page):
    home_page = get_logged_home_page
    news_page = NewsPage(home_page.driver)
    news_page.find_button_prev_page_new()


@pytest.mark.regression
def test_go_to_next_page_news(get_logged_home_page):
    home_page = get_logged_home_page
    news_page = NewsPage(home_page.driver)
    url1 = news_page.get_current_url()
    news_page.click_button_next_page_news()
    url2 = news_page.get_current_url()
    assert url1 != url2
