import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ConfirmFixPlan(BasePage):

    @allure.step("确认定投计划页面，点击确定按钮")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_fix_plan']['_confirm_btn'])

    @allure.step("暂停，恢复，终止定投计划提示框，点击确定按钮")
    def click_confirm(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_fix_plan']['_confirm'])


