import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TransferSuccessPage(BasePage):

    @allure.step("获取转出成功文案")
    def get_success_text(self):
        success_text = self.find_element(By.ID,
                                         self.get_file_from_yaml()['transfer_success_page']['_success_text']).text
        return success_text

    @allure.step("点击‘完成’")
    def click_done_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['transfer_success_page']['_done_btn'])

    @allure.step("获取转出份额")
    def get_transfer_share(self):
        text = self.find_element(By.ID, self.get_file_from_yaml()['transfer_success_page']['_transfer_share']).text
        transfer_share = self.get_numbers_from_str(text)
        return transfer_share[0]
