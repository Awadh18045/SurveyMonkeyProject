import pytest
import allure
from pages.create_new_request import CreateRequest
from utils.functions import is_element_displayed


@pytest.mark.usefixtures("setup", "website_setup")
class TestLogIn:
    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login_passed(self, config):
        log_in_page = CreateRequest(self.driver)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("THALESH-AUTOMATION", "Admin1234@")
        log_in_page.dash_board("Test 2 automation", "automation testing")
        log_in_page.new_form_creation("Automation test", "Test")
        assert not is_element_displayed(self.driver, "//span[text()='Accept']/../../..")

    def test_duplicate_view_check(self, config):
        log_in_page = CreateRequest(self.driver)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("THALESH-AUTOMATION", "Admin1234@")
        log_in_page.dash_board("Test 2 automation", "Duplicacy test")
        log_in_page.new_form_creation_dropdown("Automation test")
        validity = log_in_page.duplicate_form_view_request()
        assert validity