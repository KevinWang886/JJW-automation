import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundTransferPage(BasePage):

    @allure.step("点击转出按钮")
    def click_transfer_btn(self):
        if self.is_element_exist(element=self.get_file_from_yaml()['fund_transfer_page']['_transfer_btn']) == True:
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_transfer_page']['_transfer_btn'])
        else:
            self.log.info('没有可转出基金')

    @allure.step("获取当前持有份额")
    def get_hold_share(self):
        hold_share = self.find_element(By.ID, self.get_file_from_yaml()['fund_transfer_page']['_hold_share']).text
        return float(hold_share)

    @allure.step("获取当前可用份额")
    def get_available_share(self):
        available_share = self.find_element(By.ID, self.get_file_from_yaml()['fund_transfer_page']['_available_share']).text
        return float(available_share)

    @allure.step("获取当前净值")
    def get_nav_value(self):
        nav_value = self.find_element(By.ID, self.get_file_from_yaml()['fund_transfer_page']['_nav_value']).text
        return float(nav_value)

    @allure.step("获取当前市值")
    def get_market_value(self):
        market_value = self.find_element(By.ID, self.get_file_from_yaml()['fund_transfer_page']['_market_value']).text
        print(float(market_value))
        return float(market_value)


