import time
import pytest
from page_object.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_report_proces_page_and_find_element(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    report_proces_page.find_header_reports_proces_button()


@pytest.mark.regression
def test_go_to_plan_fact_analys(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    report_proces_page.go_to_plan_fact_analis().find_reports_settings_title()


@pytest.mark.regression
def test_go_to_fact_import(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    report_proces_page.go_to_fact_import().find_button_import_actual_from_excel()


@pytest.mark.regression
def test_go_to_plan_import(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    report_proces_page.go_to_plan_import().find_select_department()


@pytest.mark.regression
def test_count_reports_blocks(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    blocks = report_proces_page.find_reports_blocks()
    assert len(blocks) == 3
    f"Expected 6 menu elements, but found {len(blocks)}"


@pytest.mark.regression
def test_come_back_to_main_page(go_to_reports_proces_page):
    report_proces_page = go_to_reports_proces_page
    report_proces_page.find_header_reports_proces_button()
    assert isinstance(report_proces_page, HomePage)
