import pytest
from page_object.home_page import HomePage
import time


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_blue_red_books_page_and_find_element(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    assert blue_red_books_page.find_header_menu_element()


@pytest.mark.regression
def test_add_income(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    el = blue_red_books_page.click_add_income_button()
    el.find_basic_articles()


@pytest.mark.regression
def test_add_costs(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    el = blue_red_books_page.click_add_cost_button()
    el.find_costs_cost_trademarks()


@pytest.mark.regression
def test_find_structure_department(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    blue_red_books_page.open_structure_department().find_all_structure()


@pytest.mark.regression
def test_find_fist_element_of_structure_department(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    blue_red_books_page.open_structure_department().find_structure_dep_lev_1()


@pytest.mark.regression
def test_come_back_to_main_page(go_to_blue_red_books_page):
    blue_red_books_page = go_to_blue_red_books_page
    blue_red_books_page.come_back_to_main_page()
    assert isinstance(blue_red_books_page, HomePage)
