import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SetDividendPage(BasePage):

    @allure.step("点击“分红修改")
    def click_modify_dividend(self):
        if self.is_element_exist(self.get_file_from_yaml()['set_dividend_page']['_modify_dividend']) == True:
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['set_dividend_page']['_modify_dividend'])

        elif self.is_element_exist(self.get_file_from_yaml()['set_dividend_page']['_modifing']) == True:
            print(self.find_element(By.ID, self.get_file_from_yaml()['set_dividend_page']['_modifing']).text)

        else:
            self.log.info("无持仓基金")

    @allure.step("获取当前分红方式")
    def get_current_dividend(self):
        if self.is_element_exist(self.get_file_from_yaml()['set_dividend_page']['_current_dividend']) == True:
            current_dividend = self.find_element(By.ID,
                                                 self.get_file_from_yaml()['set_dividend_page']['_current_dividend']).text
            return current_dividend
        else:
            self.log.info("无持仓基金")
