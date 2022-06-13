import pytest
import allure
from pages.create_new_request import CreateRequest


@pytest.mark.usefixtures("setup", "website_setup")
class TestCases:
    def test_mandatory(self, config):
        log_in_page = CreateRequest(self.driver)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("THALESH-AUTOMATION", "Admin1234@")
        log_in_page.dash_board("Test 2 automation", "automation testing")
        result = log_in_page.mandatory_field_check("Automation test", "Test")
        assert result