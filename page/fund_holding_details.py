import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundHoldingDetails(BasePage):

        @allure.step("点击详情")
        def click_fund_detail(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_fund_details_btn'])

        @allure.step("展开")
        def expanded_menu(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_expanded_menu'])

        @allure.step("点击每日收益按钮")
        def click_everyday_income(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_everyday_income_btn'])

        @allure.step("点击交易记录按钮")
        def click_trade_records(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_trade_records_btn'])

        @allure.step("点击分红明细按钮")
        def click_profit_records(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_profit_record_btn'])

        @allure.step("点击修改分红按钮")
        def click_modify_profit(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_modify_profit_btn'])
        
        @allure.step("获取可用份额")
        def get_available_share(self):
            available_share = self.find_element(By.ID,
                                           self.get_file_from_yaml()['fund_holding_details']['_available_share']).text
            return float(available_share)

        @allure.step("点击【转换】")
        def click_transfer(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_transfer'])

        @allure.step("点击【赎回】")
        def click_redeem(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_redeem'])

        @allure.step("点击【定投】")
        def click_fix_buy(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_fix_buy'])

        @allure.step("点击[追加】")
        def click_add_buy(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_holding_details']['_add_buy'])






