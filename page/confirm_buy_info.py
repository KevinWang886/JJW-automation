import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ConfirmBuyInfo(BasePage):

    @allure.step('确认购买')
    def click_confirm_buy_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_buy_info']['_confirm_btn'])

    @allure.step('获取购买金额')
    def get_balance(self):
        buy_balance = self.find_element(By.ID, self.get_file_from_yaml()['confirm_buy_info']['_balance']).text
        return buy_balance

    @allure.step('获取下单日期')
    def get_order_date(self):
        order_date = self.find_element(By.ID, self.get_file_from_yaml()['confirm_buy_info']['_order_date']).text
        return order_date
