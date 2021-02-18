import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class MyHolding(BasePage):

        @allure.step("获取页面标题")
        def get_page_title(self):
            page_title = self.find_element(By.ID, self.get_file_from_yaml()['my_holding']['_title']).text
            return page_title

        @allure.step("获取总资产")
        def get_fund_count(self):
            total_assert = self.find_element(By.ID, self.get_file_from_yaml()['my_holding']['_total_assert']).text
            return int(total_assert)

        @allure.step("获取累计收益")
        def get_total_income(self):
            total_income = self.find_element(By.ID, self.get_file_from_yaml()['my_holding']['_total_income']).text
            return float(total_income)

        @allure.step("获取昨日收益")
        def get_yesterday_income(self):
            yesterday_income = self.find_elements(By.ID, self.get_file_from_yaml()['my_holding']['_yesterday_income'])
            return len(yesterday_income)

        @allure.step("点击基金tab")
        def click_fund_tab(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['my_holding']['_fund_tab'])

        @allure.step("点击组合tab")
        def click_group_tab(self):
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['my_holding']['_group_tab'])

        @allure.step("点击持有基金")
        def click_holding_fund(self):
            fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['my_holding']['_holding_fund_list'])
            fund_list[0].click()



