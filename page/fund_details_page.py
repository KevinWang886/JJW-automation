import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundDetailsPage(BasePage):

    @allure.step("基金详情页，获取基金净值")
    def get_fund_net(self):
        fund_net = self.find_element(By.ID, self.get_file_from_yaml()['fund_details_page']['_fund_net']).text
        return fund_net

    @allure.step("基金详情页，获取基金类型")
    def get_fund_type(self):
        fund_type = self.find_element(By.ID, self.get_file_from_yaml()['fund_details_page']['_fund_type']).text
        return fund_type

    @allure.step("基金详情页，获取基金日涨幅")
    def get_daily_range(self):
        daily_range = self.find_element(By.ID, self.get_file_from_yaml()['fund_details_page']['_daily_range']).text
        return daily_range

    @allure.step("基金详情页，点击【立即定投】")
    def click_fix_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_details_page']['_fix_buy'])

    @allure.step("基金详情页，点击【立即购买】")
    def click_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_details_page']['_buy'])
