from __future__ import annotations

import allure
import pytest

from pages.wikipedia_app import wikipedia


@allure.suite("Wikipedia Mobile Tests - iOS")
@allure.tag("ios", "search", "browserstack")
@allure.title("iOS: Wikipedia search should work")
@pytest.mark.skip(reason="iOS requires separate app upload and configuration")
class TestIOSWikipedia:

    @allure.title("iOS: Search for 'BrowserStack' on iPhone")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ios
    def test_ios_search_in_wikipedia__valid_query__should_find_results(self):
        """
        iOS test for Wikipedia search.
        Note: Requires Wikipedia iOS app uploaded to BrowserStack.
        If app is not uploaded, the test will fail with capability error.
        """
        # Given: Wikipedia iOS app is open
        wikipedia.close_onboarding()

        # When: User searches for "BrowserStack"
        # Note: iOS selectors might differ from Android
        wikipedia.search("BrowserStack")

        # Then: Search results should be displayed
        wikipedia.results_should_contain_text("BrowserStack")

        allure.attach(
            "iOS test executed on BrowserStack\n"
            "Note: Actual iOS selectors would need to be adapted for Wikipedia iOS app",
            name="ios_test_info",
            attachment_type=allure.attachment_type.TEXT
        )