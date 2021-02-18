import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ResetTradePwdPage(BasePage):
        @allure.step("输入身份证号")
        def input_id_no(self, id_no):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_id_no'], id_no)

        @allure.step("输入姓名")
        def input_name(self, name):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_name'], name)

        @allure.step("输入手机号")
        def input_mobile(self, mobile):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_mobile'], mobile)

        @allure.step("获取验证码")
        def get_code(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_get_code'])

        @allure.step("输入验证码")
        def input_verify_code(self, verify_code):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_verify_code'], verify_code)

        @allure.step("输入新密码")
        def input_pwd(self, pwd):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_pwd'], pwd)

        @allure.step("确认新密码")
        def input_confirm_pwd(self, confirm_pwd):
            self.send_keys(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_confirm_pwd'], confirm_pwd)

        @allure.step("点击【确认】")
        def click_confirm_btn(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['reset_trade_pwd_page']['_confirm_btn'])

