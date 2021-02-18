import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PrivateInfo(BasePage):
    @allure.step("同意")
    def click_agree(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['private_info']['_confirm'])

    @allure.step("获取title内容")
    def get_title(self):
        title = self.find_element(By.ID, self.get_file_from_yaml()['private_info']['_private_title']).text
        return title

    @allure.step("获取content内容")
    def get_content(self):
        content = self.find_element(By.ID, self.get_file_from_yaml()['private_info']['_private_content']).text
        return content


