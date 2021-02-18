import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ModifyDividendSuccess(BasePage):

    @allure.step('获取成功文案')
    def get_success_text(self):
        success_text = self.find_element(By.ID, self.get_file_from_yaml()['modify_dividend_success']['_success_text'])
        return success_text

    @allure.step('获取修改分红方式为')
    def get_modify_to_dividend(self):
        change_to_dividend = self.find_element(By.ID, self.get_file_from_yaml()['modify_dividend_success']['_modify_to'])
        return change_to_dividend
