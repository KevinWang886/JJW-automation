import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class UndoSuccess(BasePage):

    @allure.step("获取成功文案")
    def get_success_text(self):
        success_text = self.find_element(By.ID, self.get_file_from_yaml()['undo_success']['_success_text']).text
        return success_text

    @allure.step("获取交易内容")
    def get_trade_content(self):
        trade_content = self.find_element(By.ID, self.get_file_from_yaml()['undo_success']['_trade_content']).text
        return trade_content

    @allure.step("点击完成按钮")
    def click_done_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_undo']['_done_btn'])
