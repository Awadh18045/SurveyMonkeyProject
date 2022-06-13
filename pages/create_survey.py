import allure
from locators.locators import CreateSurveyLocators
from pages.base_page import BasePage
class CreateSurvey(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Creating Survey from the Scratch")
    def create_survey(self, survey_title):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*CreateSurveyLocators.create_survey_link).click()
        self.driver.find_element(*CreateSurveyLocators.scratch_text).click()
        self.driver.find_element(*CreateSurveyLocators.survey_name).send_keys(survey_title)
        self.driver.find_element(*CreateSurveyLocators.create_button_id).click()

    @allure.step("Assertion of survey title")
    def get_survey_title(self):
        survey = self.driver.find_element(*CreateSurveyLocators.assert_survey_title)
        return survey.text
