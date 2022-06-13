import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import AddQuestionLocators
from pages.base_page import BasePage


class AddQuestion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Adding Question")
    def add_question(self, question):
        time.sleep(5)
        self.driver.find_element(*AddQuestionLocators.question).send_keys(question)

    @allure.step("Add type of question")
    def add_type_of_question(self, question_type):
        self.driver.find_element(*AddQuestionLocators.question_type).click()
        try:
            _ = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, question_type))
            )
            self.driver.find_element_by_link_text(question_type).click()
        finally:
            pass

    @allure.step("Add options in design survey")
    def add_options(self, opt_dict):
        for ans_num, ans_value in opt_dict.items():
            self.driver.find_element(AddQuestionLocators.answer_choice_option[0],
                                     AddQuestionLocators.answer_choice_option[1].replace("%VAR%",
                                                                                         str(ans_num))).send_keys(
                ans_value)

    @allure.step("Assertion of count of question")
    def get_question_count(self):
        count = len(self.driver.find_elements(*AddQuestionLocators.assert_count_Question))
        return count

    @allure.step("Click on next question")
    def next_question(self):

        try:
            em = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(AddQuestionLocators.next)
            )
            self.driver.find_element(*AddQuestionLocators.next).click()
        finally:
            pass

    @allure.step("Click on done after creating all questions")
    def done_question(self):

        try:
            em = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(AddQuestionLocators.done_button)
            )
            self.driver.find_element(*AddQuestionLocators.done_button).click()
        finally:
            pass
