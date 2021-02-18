import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ConfirmRedeem(BasePage):

    @allure.step("获取是否顺延赎回状态")
    def get_delay_redeem_status(self):
        delay_redeem_status = self.find_element(By.ID, self.get_file_from_yaml()['confirm_redeem']['_redeem_delay']).text
        return delay_redeem_status

    @allure.step("获取赎回份额")
    def get_redeem_share(self):
        redeem_share = self.find_element(By.ID, self.get_file_from_yaml()['confirm_redeem']['_redeem_share']).text
        return redeem_share

    @allure.step("点击确认赎回")
    def click_confirm_redeem(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_redeem']['_confirm_btn'])
