import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SearchPage(BasePage):
    @allure.step("搜索框，输入搜索内容")
    def input_info(self, fund_code):
        self.send_keys(By.ID, self.get_file_from_yaml()['search_page']['_search'], fund_code)

    @allure.step("搜索框，清除输入内容")
    def clear_input(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['search_page']['_clear'])

    @allure.step("搜索框，取消搜索")
    def cancel_search(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['search_page']['_cancel'])

    @allure.step("无搜索结果时，获取页面文案")
    def no_results(self):
        no_result = self.find_element(By.ID, self.get_file_from_yaml()['search_page']['_none']).text
        return no_result

    @allure.step("搜索框，点击搜索结果")
    def click_search_result(self):
        search_results = self.find_elements(By.ID, self.get_file_from_yaml()['search_page']['_list'])
        if len(search_results) > 0:
            search_results[0].click()
        else:
            SearchPage.no_results(self)
