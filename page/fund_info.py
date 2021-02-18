import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundInfo(BasePage):

    @allure.step('点击立即购买')
    def click_buy_now(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_info']['_buy_now'])

    @allure.step('获取立即购买按钮状态')
    def get_buy_btn_status(self):
        btn_status = self.find_element(By.ID, self.get_file_from_yaml()['fund_info']['_buy_now']).\
            get_attribute("enabled")
        return btn_status

    @allure.step('点击立即定投')
    def click_fix_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_info']['_fix_buy'])

    @allure.step('获取立即定投按钮状态')
    def get_fix_btn_status(self):
        btn_status = self.find_element(By.ID, self.get_file_from_yaml()['fund_info']['_fix_buy']).\
            get_attribute("enabled")
        return btn_status

    @allure.step('点击基金名称')
    def get_fund_name(self):
        fund_name = self.find_element(By.ID, self.get_file_from_yaml()['fund_info']['_page_title']).text
        return fund_name

    @allure.step('点击基金代码')
    def get_fund_code(self):
        fund_code = self.find_element(By.ID, self.get_file_from_yaml()['fund_info']['_fund_code']).text
        return fund_code

    @allure.step('点击返回按钮')
    def click_return(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_info']['_return_btn'])

    @allure.step('点击添加自选')
    def click_add_selection(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_info']['_add_selection'])



