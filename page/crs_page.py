import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CRSPage(BasePage):

    @allure.step("点击确定按钮")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_page']['_confirm_btn'])

    @allure.step("点击仅为中国税收居民按钮")
    def click_chinese_only(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_page']['_china_only'])

    @allure.step("获取仅为中国税收居民按钮状态")
    def get_chinese_only_status(self):
        checked = self.find_element(By.ID, self.get_file_from_yaml()['crs_page']['_china_only']).get_attribute("checked")
        return checked

    @allure.step("点击仅为非中国税收居民按钮")
    def click_not_china(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_page']['_not_china'])

    @allure.step("获取仅为非中国税收居民按钮状态")
    def get_not_china_status(self):
        checked = self.find_element(By.ID, self.get_file_from_yaml()['crs_page']['_not_china']).get_attribute("checked")
        return checked

    @allure.step("点击既为中国又为其他国家或地区税收居民按钮")
    def click_all(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_page']['_all_type'])

    @allure.step("获取既为中国又为其他国家或地区税收居民按钮状态")
    def get_all_status(self):
        checked = self.find_element(By.ID, self.get_file_from_yaml()['crs_page']['_all_type']).get_attribute("checked")
        return checked
