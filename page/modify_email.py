import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ModifyEmail(BasePage):

    @allure.step("输入新邮箱")
    def input_new_email(self, email):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_email']['_new_email'], email)

    @allure.step("输入登录密码")
    def input_login_pwd(self, login_pwd):
        self.send_keys(By.ID, self.get_file_from_yaml()['modify_email']['_login_pwd'], login_pwd)

    @allure.step("点击确定按钮")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['modify_email']['_confirm_btn'])




