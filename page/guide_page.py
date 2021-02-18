import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class GuidePage(BasePage):    # 引导页

    def __init__(self, driver):   # 初始化
        super().__init__(driver)
        self.driver = driver

    @allure.step("引导页，点击【同意】")
    def click_agree_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['guide_page']['_agree'])

    @allure.step("引导页，点击【不同意】")
    def click_disagree_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['guide_page']['_cancel'])

    @allure.step("引导页，点击【跳过】")
    def click_skip_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['guide_page']['_skip'])

    @allure.step("引导页，点击【马上体验】")
    def click_go_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['guide_page']['_go_btn'])

    @allure.step("引导页，点击【立即注册】")
    def click_go_register_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['guide_page']['_go_register_btn'])





