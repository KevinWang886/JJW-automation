import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FixPlanSuccess(BasePage):

    @allure.step("获取成功信息")
    def get_success_text(self):
        success_text = self.find_element(By.ID, self.get_file_from_yaml()['fix_plan_success']['_success_text']).text
        return success_text

    @allure.step("获取定投金额")
    def get_fix_plan_amount(self):
        fix_plan_amount = self.find_element(By.ID,
                                            self.get_file_from_yaml()['fix_plan_success']['_fix_plan_amount']).text
        return fix_plan_amount

    @allure.step("点击‘完成’")
    def click_done_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fix_plan_success']['_done_btn'])
