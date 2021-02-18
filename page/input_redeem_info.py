import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class InputRedeemInfo(BasePage):

    @allure.step("输入赎回份额")
    def input_redeem_share(self, redeem_share):
        self.send_keys(By.XPATH, self.get_file_from_yaml()['input_redeem_info']['_input_redeem_share'], redeem_share)

    @allure.step("点击全部赎回")
    def click_redeem_all(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_redeem_info']['_all'])

    @allure.step("点击20%")
    def click_twenty_percent(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_redeem_info']['_twenty_percent'])

    @allure.step("点击30%")
    def click_thirty_percent(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_redeem_info']['_thirty_percent'])

    @allure.step("点击50%")
    def click_fifty_percent(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_redeem_info']['_fifty_percent'])

    @allure.step("获取水印最低赎回份额")
    def get_watermark(self):
        watermark = self.find_element(By.ID,self.get_file_from_yaml()['input_redeem_info']['_watermark']).text
        lowest_share = self.get_numbers_from_str(watermark)
        return lowest_share[0]

    @allure.step("获取当前可用份额")
    def get_available_share(self):
        available_share_text = self.find_element(By.ID,
                                                 self.get_file_from_yaml()['input_redeem_info']['_available_share']).text
        available_share = self.get_numbers_from_str(available_share_text)
        return available_share[0]

    @allure.step("点击确认赎回")
    def click_confirm_redeem_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_redeem_info']['_next_btn'])

