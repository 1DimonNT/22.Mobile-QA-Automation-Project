import allure
import pytest
from pages.wikipedia_app import wikipedia


@allure.suite("Wikipedia Mobile Tests")
@allure.tag("android", "search", "browserstack")
@allure.title("Search in Wikipedia should return results")
class TestWikipediaSearch:

    @allure.title("Search for 'BrowserStack' and verify results exist")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.android
    def test_search_in_wikipedia__valid_query__should_find_results(self):
        wikipedia.close_onboarding()
        wikipedia.search("BrowserStack")
        wikipedia.results_should_contain_text("BrowserStack")