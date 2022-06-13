import time
import allure
import pytest
from pages.add_questions_page import AddQuestion
from pages.create_survey import CreateSurvey
from pages.login_page import LogInPage
from pages.preview_page import AttemptQuestion


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

        # Assert Create Survey
        create.get_survey_title()
        assert "Quiz" == create.get_survey_title()
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
        add_question.add_question("Checkboxes")
        add_question.add_type_of_question("Checkboxes")
        add_question.add_options({"1": "1", "2": "2", "3": "3", "4": "4"})
        add_question.get_question_count() == 3

        # done question
        add_question.done_question()

        # Attempt preview questions
        attempt = AttemptQuestion(self.driver)
        attempt.preview_score()
        attempt.assert_end_preview()
        assert "That's the end of the preview!" == attempt.assert_end_preview()