import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class RedeemPage(BasePage):

        @allure.step("点击赎回按钮")
        def click_redeem_btn(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['redeem_page']['_redeem_btn'])

        @allure.step("点击返回按钮")
        def click_return_btn(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['redeem_page']['_return_btn'])

