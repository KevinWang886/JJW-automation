import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductStore(BasePage):

    @allure.step('点击兑换记录')
    def exchange_details(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_store']['_exchange_details'])

    @allure.step('点击我的奖励')
    def my_reward(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_store']['_my_reward'])

    @allure.step('点击商品')
    def product(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_store']['_product'])

    @allure.step('获取商品名称')
    def get_product_name(self):
        product_name = self.find_elements(By.ID, self.get_file_from_yaml()['product_store']['_product_name']).text
        if len(product_name) > 0:
            return product_name
        else:
            self.log.info("没有商品")
