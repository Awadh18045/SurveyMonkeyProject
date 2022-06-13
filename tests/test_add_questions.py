import time
import allure
import pytest
from pages.add_questions_page import AddQuestion
from pages.create_survey import CreateSurvey
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestCreateSurveyAddQuestions:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_add_question_function(self, config):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_home_page(config)
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("Awadh1810", "Pawadh123@")

        create = CreateSurvey(self.driver)
        create.create_survey("Quiz")

        add_question = AddQuestion(self.driver)
        # add question 1 of type MCQ
        add_question.add_question("Multiple Choice")
        add_question.add_type_of_question("Multiple Choice")
        add_question.add_options({"1": "1", "2": "2", "3": "3", "4": "4"})
        add_question.get_question_count() == 1
        add_question.next_question()

        # add question 2 of type Dropdown
        add_question.add_question("Dropdown")
        add_question.add_type_of_question("Dropdown")
        add_question.add_options({"1": "1", "2": "2", "3": "3", "4": "4"})
        add_question.get_question_count() == 2
        add_question.next_question()

        # add question 3 of type CheckBoxes
        add_question.add_question("checkboxes")
        add_question.add_type_of_question("Checkboxes")
        add_question.add_options({"1": "1", "2": "2", "3": "3", "4": "4"})
        add_question.get_question_count() == 3

        time.sleep(4)
        add_question.done_question()

        add_question.get_question_count()
        assert 3 == add_question.get_question_count()
