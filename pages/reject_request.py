import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.functions import is_element_displayed, view_and_edit_request, dashboard_elements
from locators.locators import DashBoardLocators, ApproverLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.create_new_request import CreateRequest


class RejectRequest(CreateRequest):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.open_login_page()
        self.set_user_inputs(email, password)

    def create_new_request(self):
        self.dash_board("Test 2 automation", "automation testing")
        self.new_form_creation("Automation test", "Test")
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'bold') and contains(text(),0)]").text

    def dashboard_operations(self, div_text):
        self.driver.get("https://dev.zennero.com/app/client/client-dashboard")
        WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable((By.XPATH, "//nav[contains(@class,'MuiList-root')]/div[2]")))
        self.driver.find_element(*dashboard_elements(div_text)).click()
        WebDriverWait(self.driver, 30).until(ec.presence_of_all_elements_located((By.XPATH, "//tbody/tr[2]")))
        self.driver.find_element(*DashBoardLocators.page_dropdown_button).click()
        self.driver.find_element(*DashBoardLocators.page_dropdown_button_all).click()
        time.sleep(5)

    def requester_resubmit_rejected_request(self, request_number):
        assert is_element_displayed(self.driver,
                                    "//span[contains(text(),'"+request_number+"')]/../..//div[text()='Rejected']")
        try:
            self.driver.find_element(*view_and_edit_request(request_number)).click()
        except:
            pass
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

    def approver_reject_request(self, request_number):
        try:
            self.driver.find_element(*view_and_edit_request(request_number)).click()
        except:
            pass
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Accept')]/../../..")))
        self.driver.find_element(*ApproverLocators.first_accept_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'YES')]/../..")))
        self.driver.find_element(*ApproverLocators.accept_request_yes_button).click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                (By.XPATH, "//span[contains(@class,'jr-btn')]/*/span[contains(text(),'Reject')]/../..")))
        self.driver.find_element(*ApproverLocators.reject_request1_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@id='request_comment']")))
        self.driver.find_element(*ApproverLocators.comment_box).click()
        self.driver.find_element(*ApproverLocators.comment_box).send_keys("Rejected by thalesh", Keys.TAB, Keys.ENTER)
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Reject')]/../../..")))
        self.driver.find_element(*ApproverLocators.final_reject_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@id='request_comment']")))
        self.driver.find_element(*ApproverLocators.comment_box).click()
        self.driver.find_element(*ApproverLocators.comment_box).send_keys("Rejected by thalesh", Keys.TAB, Keys.ENTER)

    def approver_accept_request(self, request_number):
        try:
            self.driver.find_element(*view_and_edit_request(request_number)).click()
        except:
            pass
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Accept')]/../../..")))
        self.driver.find_element(*ApproverLocators.first_accept_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'YES')]/../..")))
        self.driver.find_element(*ApproverLocators.accept_request_yes_button).click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(@class,'jr-btn')]/*/span[contains(text(),'Approve')]/../..")))
        self.driver.find_element(*ApproverLocators.approve_request1_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@id='request_comment']")))
        self.driver.find_element(*ApproverLocators.comment_box).click()
        self.driver.find_element(*ApproverLocators.comment_box).send_keys("Approved by thalesh", Keys.TAB, Keys.ENTER)
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Reject')]/../../..")))
        self.driver.find_element(*ApproverLocators.final_approve_button).click()
        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@id='request_comment']")))
        self.driver.find_element(*ApproverLocators.comment_box).click()
        self.driver.find_element(*ApproverLocators.comment_box).send_keys("Approved by thalesh", Keys.TAB, Keys.ENTER)

