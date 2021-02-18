import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class BuyFundSuccess(BasePage):

    @allure.step('获取成功文案')
    def get_success_text(self):
        success_text = self.find_element(By.ID, self.get_file_from_yaml()['buy_fund_success']['_success_text']).text
        return success_text

    def click_done_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['buy_fund_success']['_done_btn'])

