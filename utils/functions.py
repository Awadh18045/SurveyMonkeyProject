from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
import json

CONFIG_PATH = "../config.json"


def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


def get_driver(config):
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])
    driver.implicitly_wait(config["timeout"])
    return driver


def is_element_displayed(driver, locator):
    try:
        driver.find_element(By.XPATH, locator)
        return True
    except:
        return False


def view_and_edit_request(request_number):
    view_request_button = (By.XPATH,
                    "//span[contains(text(),'"+request_number+"')]/../..//*[local-name()='svg' and contains(@class, 'MuiSvgIcon-colorPrimary')]")
    return view_request_button


def dashboard_elements(element_name):
    clint_dashboard = (By.XPATH, "//nav[contains(@class,'MuiList-root')]//span[contains(text(),'" +element_name+"')]")
    return clint_dashboard


def duplicate_data_request_number(req_no):
    request_number = (By.XPATH, "//tbody//span[contains(text(),'"+req_no+"')]")
    return request_number


def adjust_travellers_number(travellers_input_val, num, subtract_btn, add_btn):
    while travellers_input_val > num:
        subtract_btn.click()
        travellers_input_val -= 1
    while travellers_input_val < num:
        add_btn.click()
        travellers_input_val += 1


def set_travellers_number(driver, num, form_loc, params: list):
    travellers_number_input = driver.find_element(*getatr(form_loc, params[0]))
    travellers_input_val = int(travellers_number_input.get_attribute("value"))
    add_btn = driver.find_element(*getattr(form_loc, params[1]))
    subtract_btn = driver.find_element(*getattr(form_loc, params[2]))
    adjust_travellers_number(travellers_input_val, num, subtract_btn, add_btn)


def get_datestamp(driver, form_loc, params: list):
    datestamps = driver.find_elements(*getattr(form_loc, params[0]))
    for datestamp in datestamps:
        if datestamp.is_displayed():
            current_datestamp = datestamp.text
            return current_datestamp


def click_displayed_datestamp(datestamps):
    for datestamp in datestamps:
        if datestamp.is_displayed():
            datestamp.click()
            break
