import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HotFundPage(BasePage):

    @allure.step("获取页面标题")
    def get_page_title(self):
        page_title = self.find_element(By.ID, self.get_file_from_yaml()['hot_fund_page']['_page_title']).text
        return page_title

    @allure.step("获取基金名称")
    def get_fund_name(self):
        fund_name = self.find_elements(By.ID, self.get_file_from_yaml()['hot_fund_page']['_fund_name'])
        if len(fund_name) > 0:
            return fund_name[0].text
        else:
            self.log.info("优选基金页面无基金")
