import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ModifyMobile(BasePage):

    @allure.step("输入身份证号")
    def input_id_no(self, id_no):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_id_no'], id_no)

    @allure.step("输入姓名")
    def input_name(self, name):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_name'], name)

    @allure.step("输入当前手机号")
    def input_current_mobile(self, current_mobile):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_current_mobile'], current_mobile)

    @allure.step("输入新手机号")
    def input_new_mobile(self, new_mobile):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_new_mobile'], new_mobile)

    @allure.step("获取短信验证码")
    def get_verify_code(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['modify_mobile']['_get_code'])

    @allure.step("输入验证码")
    def input_verify_code(self, verify_code):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_input_code'], verify_code)

    @allure.step("输入输入交易密码")
    def input_trade_pwd(self, trade_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_mobile']['_trade_pwd'], trade_pwd)

    @allure.step("点击确认按钮")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['modify_mobile']['_confirm_btn'])
