import allure
import pytest

from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestLogIn:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login_passed(self, config):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_home_page(config)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("Awadh1810", "Pawadh123@")
        assert "dashboard" in log_in_page.get_current_url(), "failed to verify dashboard after login"
