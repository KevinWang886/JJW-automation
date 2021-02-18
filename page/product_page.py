from selenium.webdriver.common.by import By
from base.base_page import BasePage
import allure


class ProductPage(BasePage):

    @allure.step("产品页，为您推荐，点击【立即购买】")
    def click_suggest_fund(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_suggest_fund_buy'])

    @allure.step("产品页，获取立即开户按钮文案")
    def get_btn_text(self):
        btn_text = self.find_element(By.ID, self.get_file_from_yaml()['product_page']['_btn_text']).text
        return btn_text

    @allure.step("产品页，点击【立即开户】按钮")
    def click_register_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_register'])

    @allure.step("产品页，点击【名人堂】按钮")
    def click_famous_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_famous_btn'])

    @allure.step("产品页，点击【驾驶室】按钮")
    def click_driver_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_driver_btn'])

    @allure.step("产品页，点击【我的】进入我的页面")
    def go_to_mine_page(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_mine_btn'])

    @allure.step("产品页，点击【基金超市】进入基金超市")
    def click_fund_market(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_fund_market'])

    @allure.step("产品页，点击【搜索】按钮")
    def click_search_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_search_btn'])

    @allure.step("产品页，关闭广告")
    def close_ad(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_ad_close'])

    @allure.step("产品页，点击广告进入名人堂")
    def click_ad(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['product_page']['_ad'])

    @allure.step("获取【产品】的状态")
    def get_product_btn_status(self):
        product_btn_status = self.find_element(By.ID,
                                    self.get_file_from_yaml()['product_page']['_product_btn']).get_attribute("checked")
        return product_btn_status

    def go_to_different_page(self, tag):
        if tag == 0:
            ProductPage.click_search_btn(self)
        elif tag == 1:
            ProductPage.go_to_mine_page(self)
        elif tag == 2:
            ProductPage.click_famous_btn(self)
        elif tag == 3:
            ProductPage.click_driver_btn(self)




