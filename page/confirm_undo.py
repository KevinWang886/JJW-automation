import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ConfirmUndo(BasePage):

    @allure.step("点击确认撤单按钮")
    def click_confirm_undo_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['confirm_undo']['_confirm_undo_btn'])

    @allure.step("获取交易状态")
    def get_trade_status(self):
        trade_status = self.find_element(By.ID, self.get_file_from_yaml()['confirm_undo']['_trade_status']).text
        return trade_status
