import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ModifyDividendPage(BasePage):

    @allure.step("选择分红方式")
    def select_dividend_method(self):
       self.find_element_and_click(By.ID,self.get_file_from_yaml()['modify_dividend_page']['_dividend_imageview'])

    @allure.step("点击确认按钮")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['modify_dividend_page']['_confirm_modify_btn'])
