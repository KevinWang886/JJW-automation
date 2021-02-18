import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundTradePage(BasePage):

    @allure.step('基金交易，点击买基金')
    def buy_fund(self):
       self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_trade']['_buy_fund'])

    @allure.step('基金交易，点击卖基金')
    def redeem_fund(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_trade']['_redeem_fund'])

    @allure.step('基金交易，点击转换基金')
    def transfer_fund(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_trade']['_transfer_fund'])

    @allure.step('基金交易，点击基金撤单')
    def trade_undo(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_trade']['_trade_undo'])

    @allure.step('基金交易，点击设置分红')
    def set_dividend(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_trade']['_set_dividend'])
