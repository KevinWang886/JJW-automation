import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class SelectTransferFund(BasePage):

    @allure.step("输入转出份额")
    def input_transfer_share(self, share):
            self.send_keys(By.XPATH, self.get_file_from_yaml()['select_transfer_fund']['_input_share'], share)

    @allure.step("获取水印")
    def get_watermark_text(self):
        watermark = self.find_element(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_hint_text']).text
        lowest_share = self.get_numbers_from_str(watermark)
        return lowest_share[0]

    @allure.step("获取当前可用份额")
    def get_available_share(self):
        available_share_text = self.find_element(By.ID,
                                            self.get_file_from_yaml()['select_transfer_fund']['_available_share']).text
        available_share = self.get_numbers_from_str(available_share_text)
        return available_share[0]

    @allure.step("点【全部】")
    def click_transfer_all(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_all_transfer'])

    @allure.step("点【20%】")
    def click_transfer_twenty(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_twenty_percent'])

    @allure.step("点【30%】")
    def click_transfer_thirty(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_thirty_percent'])

    @allure.step("点【50%】")
    def click_transfer_fifty(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_fifty_percent'])

    @allure.step("点击转入基金")
    def click_transfer_fund(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_select_transfer_btn'])
    #
    # @allure.step("勾选协议")
    # def click_checkbox(self):
    #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_checkbox'])

    @allure.step("点击‘确定'")
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_next_btn'])

    @allure.step("选择转入基金")
    def select_fund(self):
        fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_fund_list'])
        if len(fund_list) > 0:
            fund_list[-1].click()
        else:
            self.log.info("无可转入基金")

    @allure.step("风险提示，点【取消】")
    def cancel_tip(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_cancel_btn'])

    @allure.step("风险提示，点【确定】")
    def confirm_tip(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['select_transfer_fund']['_confirm_btn'])





