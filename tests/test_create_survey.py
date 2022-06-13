import allure
import pytest

from pages.create_survey import CreateSurvey
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestCreateSurvey:

    @allure.title("Creating Survey")
    @allure.description("This is test of create survey")
    def test_create_survey_function(self, config):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_home_page(config)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("Awadh1810", "Pawadh123@")
        create = CreateSurvey(self.driver)
        create.create_survey("Quiz")
        create.get_survey_title()
        assert "Quiz" == create.get_survey_title()
