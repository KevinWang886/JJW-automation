import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step("输入手机号")
    def input_mobile(self, mobile):
        self.send_keys(By.XPATH, self.get_file_from_yaml()['register_page']['_mobile'], mobile)

    @allure.step("获取验证码")
    def get_code(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['register_page']['_send_code'])

    @allure.step("输入验证码")
    def input_verify_code(self, verify_code):
        self.send_keys(By.XPATH, self.get_file_from_yaml()['register_page']['_verify_code'], verify_code)

    @allure.step("输入登录密码")
    def input_pwd(self, pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['register_page']['_pwd'], pwd)

    @allure.step("输入确认密码")
    def input_confirm_pwd(self, confirm_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['register_page']['_confirm_pwd'], confirm_pwd)

    @allure.step("点击下一步按钮")
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['register_page']['_next_btn'])
