import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CommonBlankPage(BasePage):

    @allure.step('点击我要购买')
    def click_buy_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['common_blank_page']['_buy_btn'])

    @allure.step('点击我要定投')
    def click_fix_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['common_blank_page']['_fix_buy_btn'])

    @allure.step('获取页面信息‘您还没有买过基金哦’')
    def get_message(self):
        message = self.find_element(By.ID, self.get_file_from_yaml()['common_blank_page']['_message']).text
        return message
