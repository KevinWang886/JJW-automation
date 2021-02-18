import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class AccountManagementPage(BasePage):

    @allure.step("点击【返回】")
    def click_back_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_back_btn'])

    @allure.step("点击【个人资料】")
    def click_personal_info(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_personal_info'])

    @allure.step("点击【手机号】")
    def click_mobile_number(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_mobile_number'])

    @allure.step("点击【银行卡】")
    def click_bank_card_count(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_bank_card_count'])

    @allure.step("点击【风险测评")
    def click_personal_risk(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_personal_risk'])

    @allure.step("点击【更多】")
    def click_more(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_more'])

    @allure.step("点击【安全退出】")
    def click_logout(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_logout'])

    @allure.step("点击【确定】确认退出登录")
    def confirm_logout(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_confirm_logout'])

    @allure.step("点击【取消】取消退出登录")
    def cancel_logout(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_cancel_logout'])

    @allure.step("获取手机号")
    def get_phone_number(self):
        phone_number = \
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_phone_number'])
        return phone_number.text

    @allure.step("获取银行卡数量")
    def get_card_count(self):
        card_count = \
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['account_management_page']['_card_count'])
        return card_count.text
