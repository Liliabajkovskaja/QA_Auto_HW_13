import time
from selenium.webdriver.common.by import By
from page_object.home_page import HomePage


class NewsPage(HomePage):
    news_artickles = "//div[contains(@class,'news_article')]"
    news_text = "(//div[contains(@class,'m-10 news-item-page')]//p)[3]"
    news_titles = "//div[contains(@class,'m-10 news-item-page')]/h1"
    count_people_viewed = "(//span[contains(@class,'read_news')])[2]"
    button_prev_page_new = "//li[contains(@class,'prev disabled')]"
    button_next_page_new = "//li[contains(@class,'next')]"

    def __init__(self, driver):
        super().__init__(driver)

    def find_news(self):
        return self.elements_are_visible((By.XPATH, self.news_artickles))

    def find_news_titles(self):
        return self.elements_are_visible((By.XPATH, self.news_titles))

    def find_button_prev_page_new(self):
        return self.element_is_visible((By.XPATH, self.button_next_page_new))

    def click_button_next_page_news(self):
        self.click_button((By.XPATH, self.button_next_page_new))

    def read_news(self, number_news):
        new = self.get_element_by_number((By.XPATH, self.news_artickles), number_news)
        new.click()
        return self

    def get_text_from_news(self):
        self.get_texts((By.XPATH, self.news_text))
        return self

    def find_count_people_viewed(self):
        self.get_texts((By.XPATH, self.count_people_viewed))
        return self
