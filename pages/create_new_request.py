import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.locators import LogInLocators, DashBoardLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import AcceptRequestLocators
from utils.functions import is_element_displayed, dashboard_elements, duplicate_data_request_number
from selenium.webdriver.common.action_chains import ActionChains


class CreateRequest(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening surveymonkey website")
    def open_login_page(self):
        self.driver.get("https://www.surveymonkey.com/user/sign-in")

    @allure.step("Login with email: '1'")
    def set_user_inputs(self, email, password):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*LogInLocators.domain_automation).click()
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(*LogInLocators.password_input).send_keys(password, Keys.ENTER)
        WebDriverWait(self.driver, 30).until(
            ec.visibility_of_all_elements_located((By.XPATH, "//nav[contains(@class,'MuiList-root')]/div[2]")))

    @allure.step("Performing dashboard operations")
    def dash_board(self, ticket_discription, div_text):
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//nav[contains(@class,'MuiList-root')]/div[2]")))
        self.driver.find_element(*dashboard_elements(div_text)).click()
        self.driver.find_element(*DashBoardLocators.new_ticket).click()
        self.driver.find_element(*DashBoardLocators.new_ticket_description).click()
        self.driver.find_element(*DashBoardLocators.new_ticket_description).send_keys(ticket_discription)

        try:
            self.driver.find_element(*DashBoardLocators.ticket_description_submit).click()
        except:
            pass

        time.sleep(5)

    @allure.step("Creating new form")
    def new_form_creation(self, form_title, form_data):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*DashBoardLocators.add_new_form).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).send_keys(form_title)
        try:
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//button[@id='submit']")))
            self.driver.find_element(*DashBoardLocators.add_form_submit_button).click()
        except:
            pass
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//input[@id='eocwsxj-thaleshName']")))
        self.driver.find_element(*DashBoardLocators.form_field).click()
        self.driver.find_element(*DashBoardLocators.form_field).send_keys(form_data)
        try:
            WebDriverWait(self.driver, 30).until(
                ec.presence_of_element_located((By.XPATH, "//div[@id='en91df']/button")))
            time.sleep(5)
            self.driver.find_element(*DashBoardLocators.form_field_submit).click()
        except:
            pass
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//span/span[text()='Submit']/../../..")))
        self.driver.find_element(*DashBoardLocators.final_form_submit).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='heading' and contains(text(),'Submitted')]")))

    def mandatory_field_check(self, form_title, form_data):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*DashBoardLocators.add_new_form).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).send_keys(form_title)
        try:
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//button[@id='submit']")))
            self.driver.find_element(*DashBoardLocators.add_form_submit_button).click()
        except:
            pass
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//label[contains(@class,'field-required')]/../div")))
        self.driver.find_element(*DashBoardLocators.mandatory_field).click()
        self.driver.find_element(*DashBoardLocators.mandatory_field).send_keys(form_data)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@id='en91df']/button")))
        self.driver.find_element(*DashBoardLocators.mandatory_field).click()
        self.driver.find_element(*DashBoardLocators.mandatory_field).clear()
        try:
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//div[@id='en91df']/button")))
            time.sleep(3)
            self.driver.find_element(*DashBoardLocators.form_field_submit).click()
        except:
            return True

    def RequestAccept(self):

        try:
            self.driver.find_element(*AcceptRequestLocators.bell_icon_).click()
        except:
            self.driver.implicitly_wait(10)

        time.sleep(5)
        try:
            self.driver.find_element(*AcceptRequestLocators.first_notification_).click()

        except:
            pass
            self.driver.implicitly_wait(10)
        time.sleep(5)
        try:
            self.driver.find_element(*AcceptRequestLocators.accept_button).click()
        except:
            self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element(*AcceptRequestLocators.yes_button).click()

    def checkApprovedrequest(self):

        try:
            self.driver.find_element(*AcceptRequestLocators.bell_icon_).click()
        except:
            self.driver.implicitly_wait(10)

        time.sleep(5)
        try:
            self.driver.find_element(*AcceptRequestLocators.first_notification_).click()
        except:
            pass
            self.driver.implicitly_wait(10)
        time.sleep(10)
        assert not is_element_displayed(self.driver,
                                        "//span[contains(text(),'Accept')]")

    @allure.step("Creating new form")
    def new_form_creation_dropdown(self, form_title):
        new_request_number = self.driver.find_element(By.XPATH, "//div[contains(@class,'bold') and contains(text(),0)]").text
        self.driver.find_element(*DashBoardLocators.add_new_form).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).click()
        self.driver.find_element(*DashBoardLocators.add_form_title).send_keys(form_title, Keys.ENTER)
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//div[contains(@class,'selection dropdown')]")))
        self.driver.find_element(*DashBoardLocators.form_dropdown).click()
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//div[@id='choices--ejgt9sg-funcArea-item-choice-1']")))
            self.driver.find_element(*DashBoardLocators.form_dropdown_1).click()
        except:
            pass
        try:
            time.sleep(5)
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//div[@id='en91df']/button")))
            self.driver.find_element(*DashBoardLocators.form_field_submit).click()
        except:
            pass

    def duplicate_form_view_request(self):
        time.sleep(2)
        request_number_1 = self.driver.find_element(By.XPATH, "//tbody//span[contains(text(),'')]").text
        try:
            self.driver.find_element(*duplicate_data_request_number(request_number_1)).click()
            WebDriverWait(self.driver, 30).until(
                ec.element_to_be_clickable((By.XPATH, "//span[text()='View request']")))
            self.driver.find_element(*DashBoardLocators.duplicate_request_view_request_button).click()
        except:
            pass
        copy_request_number_1 = self.driver.find_element(By.XPATH,
                                                         "//div[contains(@class,'bold') and contains(text(),0)]").text
        if request_number_1 == copy_request_number_1:
            return True
        else:
            return False



