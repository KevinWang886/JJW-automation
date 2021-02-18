import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class BindCardPage(BasePage):

    @allure.step("点击银行卡")
    def click_bank_card(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card_page']['_bank_btn'])

    @allure.step("选择银行卡")
    def select_card(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['bind_card_page']['_bank_name'])

    @allure.step("输入银行卡号")
    def input_card_no(self, card_no):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card_page']['_card_no'], card_no)

    @allure.step("输入手机号")
    def input_mobile_no(self, mobile_no):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card_page']['_mobile_no'], mobile_no)

    @allure.step("获取验证码")
    def get_verify_code(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card_page']['_get_code'])

    @allure.step("输入验证码")
    def input_verify_code(self, verify_code):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card_page']['_verify_code'], verify_code)

    @allure.step("输入交易密码")
    def input_trade_pwd(self, trade_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card_page']['_trade_pwd'], trade_pwd)

    @allure.step("点击确定")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card_page']['_confirm_btn'])



