import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ConfirmTransferPage(BasePage):

    @allure.step("获取转出份额")
    def get_transfer_share(self):
        text = self.find_element(By.ID, self.get_file_from_yaml()['confirm_transfer_page']['_transfer_share']).text
        transfer_share = self.get_numbers_from_str(text)
        return transfer_share[0]

    @allure.step("点击‘确认转换’")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_transfer_page']['_confirm_transfer_btn'])
