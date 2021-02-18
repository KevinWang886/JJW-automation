import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundMarketPage(BasePage):

    @allure.step("基金超市，基金排行")
    def click_fund_rank(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_fund_rank'])

    @allure.step("基金超市，明星基金")
    def click_star_fund(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_star_fund'])

    @allure.step("基金超市，新手学堂")
    def click_new_school(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_new_school'])

    @allure.step("基金超市，信息披露")
    def click_info_disclosure(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_information_disclosure'])

    @allure.step("基金超市，推荐tab")
    def click_recommend_tab(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_recommend'])

    @allure.step("基金超市，热门tab")
    def click_hot_tab(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_hot'])

    @allure.step("基金超市，热门tab")
    def click_item_tab(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_market_page']['_item'])

    @allure.step("基金超市，获取基金列表")
    def get_tab_fund_list(self):
        fund_list = self.find_elements(By.XPATH, self.get_file_from_yaml()['fund_market_page']['_tab_fund_list'])
        return len(fund_list)

