import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):
    @allure.step("首页，点击【基金超市】")
    def click_fund_market(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_fund_market'])

    @allure.step("首页，点击【我的】")
    def click_mine_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_mine_page'])

    @allure.step("首页，点击【搜索】")
    def click_search_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_search_btn'])

    @allure.step("首页，50秒开户")
    def click_quick_reg_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_quick_reg'])

    @allure.step("获取按钮文案")
    def get_quick_reg_btn_text(self):
        btn_text = self.find_element(By.ID, self.get_file_from_yaml()['home_page']['_btn_text']).text
        return btn_text

    @allure.step("首页，优选基金")
    def click_hot_fund_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_hot_fund'])

    @allure.step("首页，新发基金")
    def click_new_fund_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_new_fund'])

    @allure.step("首页，活期理财")
    def click_hqlc(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_hqlc'])

    @allure.step("首页，工资定投")
    def click_gzdt(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_gzdt'])

    @allure.step("首页，平台实力")
    def click_ptsl(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_ptsl'])

    @allure.step("首页，获取推荐基金数量")
    def get_advise_fund_count(self):
        advise_fund_count = self.find_elements(By.ID, self.get_file_from_yaml()['home_page']['_advise_funds'])
        return len(advise_fund_count)

    @allure.step("首页，点击推荐基金")
    def click_advise_fund(self):
        fund_items = self.find_elements(By.ID, self.get_file_from_yaml()['home_page']['_fund_item_btn'])
        fund_items[0].click()

    @allure.step("首页，理财咨询，点击更多按钮")
    def click_more_btn(self):
        self.slip_up()
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['home_page']['_more_btn'])
