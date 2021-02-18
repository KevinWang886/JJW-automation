import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TradeUndo(BasePage):

    @allure.step("点击撤单按钮")
    def click_undo_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_undo']['_undo_btn'])

