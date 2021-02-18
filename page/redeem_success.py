import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class RedeemSuccess(BasePage):

    @allure.step("获取成功文案")
    def get_success_text(self):
        success_text = self.find_element(By.ID, self.get_file_from_yaml()['redeem_success']['_success_text']).text
        return success_text

    @allure.step("获取赎回份额")
    def get_redeem_share(self):
        redeem_share = self.find_element(By.ID, self.get_file_from_yaml()['redeem_success']['_redeem_share']).text
        return redeem_share

    @allure.step("点击完成按钮")
    def click_done_btn(self):
        self.find_element(By.ID, self.get_file_from_yaml()['redeem_success']['_done_btn'])

    @allure.step("点击查看交易记录按钮")
    def click_trade_record_btn(self):
        self.find_element(By.ID, self.get_file_from_yaml()['redeem_success']['_trade_record'])

