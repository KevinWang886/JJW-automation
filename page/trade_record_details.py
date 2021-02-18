import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TradeRecordDetails(BasePage):

    @allure.step("获取交易状态")
    def get_trade_status(self):
        trade_status = self.find_element(By.ID, self.get_file_from_yaml()['trade_record_details']['_trade_status']).text
        return trade_status

    @allure.step("获取交易类型")
    def get_trade_type(self):
        trade_type = self.find_element(By.ID, self.get_file_from_yaml()['trade_record_details']['_trade_type']).text
        return trade_type

    @allure.step("获取基金类型")
    def get_fund_type(self):
        fund_type = self.find_element(By.ID, self.get_file_from_yaml()['trade_record_details']['_fund_type']).text
        return fund_type

    @allure.step("获取交易状态")
    def get_status(self):
        status = self.find_element(By.ID, self.get_file_from_yaml()['trade_record_details']['_status']).text
        return status
