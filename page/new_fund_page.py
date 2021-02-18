import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class NewFundPage(BasePage):

    @allure.step("获取页面标题")
    def get_page_title(self):
        page_title = self.find_element(By.ID, self.get_file_from_yaml()['new_fund_page']['_page_title']).text
        return page_title
