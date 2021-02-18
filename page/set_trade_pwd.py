import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SetTradePwd(BasePage):

    @allure.step("输入交易密码")
    def input_trade_pwd(self, trade_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['set_trade_pwd']['_trade_pwd'], trade_pwd)

    @allure.step("输入确认交易密码")
    def input_confirm_trade_pwd(self, confirm_trade_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['set_trade_pwd']['_confirm_trade_pwd'], confirm_trade_pwd)

    @allure.step("点击下一步按钮")
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['set_trade_pwd']['_next_btn'])
