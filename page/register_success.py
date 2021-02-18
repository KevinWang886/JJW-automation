import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class RegisterSuccess(BasePage):

    @allure.step("获取成功信息")
    def get_success_text(self):
        success_text =  self.find_element(By.XPATH, self.get_file_from_yaml()['register_success']['_success_text']).text
        return success_text
