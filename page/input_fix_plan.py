import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class InputFixPlan(BasePage):

    @allure.step("获取水印文案")
    def get_watermark(self):
        watermark = self.find_element(By.ID, self.get_file_from_yaml()['input_fix_plan']['_watermark']).text
        lowest_amount = self.get_numbers_from_str(watermark)
        return lowest_amount[0]

    @allure.step("输入定投金额")
    def input_fix_amount(self, fix_amount):
        self.send_keys(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_amount'], fix_amount)

    @allure.step("获取当前定投周期")
    def get_fix_cycle(self):
        fix_cycle = self.find_element(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_cycle_value']).text
        return fix_cycle

    @allure.step("获取当前定投日期")
    def get_fix_date(self):
        fix_date = self.find_element(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_date_value']).text
        return fix_date

    @allure.step("获取当前扣款类型")
    def get_pay_fail_value(self):
        pay_fail_value = self.find_element(By.ID, self.get_file_from_yaml()['input_fix_plan']['_pay_fail_value']).text
        return pay_fail_value

    @allure.step("选择定投周期")
    def select_fix_cycle(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_cycle'])

    @allure.step("选择定投日期")
    def select_fix_date(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_date'])

    @allure.step("点击确定")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_confirm_btn'])

    @allure.step('取消提示')
    def cancel_alert(self):
        if self.is_element_exist(self.get_file_from_yaml()['input_fix_plan']['_cancel_alert']) == True:
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_cancel_alert'])
        else:
            print("进入到确认定投计划页面")

    @allure.step('确认提示')
    def confirm_alert(self):
        # if self.is_element_exist(self.get_file_from_yaml()['input_fix_plan']['_confirm_alert']) == True:
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_confirm_alert'])
        # else:
        #     print("进入到确认定投计划页面")

    @allure.step("选择扣款类型")
    def select_pay_fail_type(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_pay_fail'])

    @allure.step("勾选协议")
    def click_checkbox(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_checkbox'])

    @allure.step("点击下一步")
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_next_btn'])
        #
        # # 如果不存在定投周期，就默认选中每月
        # if self.is_element_exist(self.get_file_from_yaml()['input_fix_plan']['_fix_cycle_value']) == False:
        #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_cycle'])
        #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_confirm_btn'])
        # else:
        #     if InputFixPlan.select_fix_cycle == '每月':   # 如果当日定投周期已选择每月，进入定投周期，选择每周
        #         self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_cycle'])
        #         self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['input_fix_plan']['_picker_box'])
        #         self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_confirm_btn'])
        #     else:
        #         self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_fix_cycle'])
        #         self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['input_fix_plan']['_picker_box'])
        #         self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_fix_plan']['_confirm_btn'])


