import time
import pytest
from page_object.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_jd_page_and_find_element(go_to_jd_page):
    jd_page = go_to_jd_page
    time.sleep(1)
    jd_page.find_header_dj_button()


@pytest.mark.regression
def test_search_position_by_input(go_to_jd_page):
    jd_page = go_to_jd_page
    time.sleep(1)
    jd_page.set_text_into_search_input()
    jd_page.find_php_developer_element()


@pytest.mark.regression
def test_sort_by_position(go_to_jd_page):
    jd_page = go_to_jd_page
    time.sleep(3)
    jd_page.sort_by_position().find_last_element_alfabet()



@pytest.mark.regression
def test_count_table_grid_items(go_to_jd_page):
    jd_page = go_to_jd_page
    items = jd_page.find_table_grid_items()
    assert len(items) == 6
    f"Expected 6 menu elements, but found {len(items)}"


@pytest.mark.regression
def test_come_back_to_main_page(go_to_jd_page):
    jd_page = go_to_jd_page
    jd_page.come_back_to_main_page()
    assert isinstance(jd_page, HomePage)
