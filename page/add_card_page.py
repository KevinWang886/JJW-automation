import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class AddCardPage(BasePage):

    @allure.step("点击添加银行卡")
    def click_add_card(self):
        # 判断添加银行卡按钮是否在当前页面，如果存在，点击添加按钮
        if self.is_element_exist(self.get_file_from_yaml()['add_card_page']['_add_card_btn']) == True:
            self.find_element_and_click(By.ID, self.get_file_from_yaml()['add_card_page']['_add_card_btn'])
        else:   # 如果添加按钮不再当前页面，向下滑动页面
            self.slip_up()
            # 判断添加银行卡按钮是否在当前页面，如果存在，点击添加按钮
            if self.is_element_exist(self.get_file_from_yaml()['add_card_page']['_add_card_btn']) == True:
                self.find_element_and_click(By.ID, self.get_file_from_yaml()['add_card_page']['_add_card_btn'])
            else:   # 如果添加按钮不再当前页面，向下滑动页面
                self.slip_up()
                self.find_element_and_click(By.ID, self.get_file_from_yaml()['add_card_page']['_add_card_btn'])

    @allure.step("点击更换")
    def click_change_card(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['add_card_page']['_change_btn'])

    @allure.step("点击解绑")
    def click_unbind_card(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['add_card_page']['_unbind_btn'])

    @allure.step("获取卡的状态")
    def get_card_status(self):
        card_status = self.find_element(By.ID, self.get_file_from_yaml()['add_card_page']['_status']).text
        return card_status

    @allure.step("获取卡的名称")
    def get_card_name(self):
        card_name = self.find_elements(By.ID, self.get_file_from_yaml()['add_card_page']['_bank_name']).text
        return card_name[0]
