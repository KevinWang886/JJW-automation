import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TradeQueryPage(BasePage):

    @allure.step('点击持仓明细')
    def click_trade_details(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_query']['_hold_details'])

    @allure.step('点击交易申请记录')
    def click_apply_records(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_query']['_apply_records'])

    @allure.step('点击交易确认记录')
    def click_confirm_records(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_query']['_confirm_records'])
