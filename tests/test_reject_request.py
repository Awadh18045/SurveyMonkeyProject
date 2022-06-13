import pytest
import allure
from pages.reject_request import RejectRequest
from utils.functions import get_driver


@pytest.mark.usefixtures("setup", "website_setup")
class TestLogIn:
    @allure.title("Login and reject the request by approver.")
    @allure.description("This is test of rejection of a request and checking weather the status is updated to rejected or not")
    def test_reject_request(self, config):
        requester = RejectRequest(self.driver)
        requester.login("THALESH-AUTOMATION", "Admin1234@")
        request_number = requester.create_new_request()
        approver_driver = get_driver(config)
        approver = RejectRequest(approver_driver)
        approver.login("APPROVER-TEST", "Admin1234@")
        approver.dashboard_operations("automation testing")
        approver.approver_reject_request(request_number)
        requester.dashboard_operations("automation testing")
        requester.requester_resubmit_rejected_request(request_number)
