import allure
import pytest
from pages.wikipedia_app import wikipedia


@allure.suite("Wikipedia Mobile Tests")
@allure.tag("android", "article", "browserstack")
@allure.title("Click on article should open article page")
class TestWikipediaArticleClick:

    @allure.title("Search and click on article result")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.android
    def test_article_click__search_and_click_result__should_open_article(self):
        wikipedia.close_onboarding()
        wikipedia.search("Selenium WebDriver")
        wikipedia.results_should_contain_text("Selenium")
        wikipedia.click_first_result()
        wikipedia.article_should_be_opened()