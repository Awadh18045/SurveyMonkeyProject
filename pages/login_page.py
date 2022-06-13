import time

import allure

from locators.locators import LogInLocators
from pages.base_page import BasePage


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Opening login page")
    def open_login_page(self):
        self.driver.find_element(*LogInLocators.login_link).click()

    @allure.step("Login with username and password")
    def set_user_inputs(self, username, password):
        self.driver.find_element(*LogInLocators.user_input).clear()
        self.driver.find_element(*LogInLocators.user_input).send_keys(username)
        self.driver.find_element(*LogInLocators.password_input).clear()
        self.driver.find_element(*LogInLocators.password_input).send_keys(password)
        self.driver.find_element(*LogInLocators.login_button).click()

    @allure.step("To assert current url")
    def get_current_url(self):
        time.sleep(5)
        url = self.driver.current_url
        return url
