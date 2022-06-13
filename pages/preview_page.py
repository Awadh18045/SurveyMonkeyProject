import time

import allure

from locators.locators import AttemptQuestionsLocators
from pages.base_page import BasePage


class AttemptQuestion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Attempt Questions")
    def preview_score(self):
        self.driver.find_element(*AttemptQuestionsLocators.preview_score_click).click()
        self.driver.switch_to.frame(self.driver.find_element(*AttemptQuestionsLocators.frame_id))
        self.driver.find_element(*AttemptQuestionsLocators.answer_q1_click).click()
        self.driver.find_element(*AttemptQuestionsLocators.answer_q2_click).click()
        self.driver.find_element(*AttemptQuestionsLocators.answer_q3b_click).click()
        self.driver.find_element(*AttemptQuestionsLocators.answer_q3c_click).click()
        self.driver.find_element(*AttemptQuestionsLocators.done_button).click()

    @allure.step("Assertion of end of preview")
    def assert_end_preview(self):
        self.driver.switch_to.default_content()
        time.sleep(2)
        assert_message = (self.driver.find_element(*AttemptQuestionsLocators.assert_message)).text
        time.sleep(2)
        return assert_message
