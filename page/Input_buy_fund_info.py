import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class InputBuyFundInfo(BasePage):

    @allure.step('输入购买金额')
    def input_buy_amount(self, amount):
        self.send_keys(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_input_amount'], amount)

    @allure.step('勾选协议')
    def check_announcement(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_checkbox'])

    @allure.step('点击下一步')
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_confirm_btn'])

    @allure.step("获取按钮的状态")
    def get_next_btn_status(self):
        btn_status = self.find_element(By.ID,
                            self.get_file_from_yaml()['input_buy_fund_info']['_confirm_btn']).get_attribute("enabled")
        return btn_status

    @allure.step("获取超银行卡限额提示")
    def get_amount_limit_text(self):
        amount_limit_text = self.find_element(By.ID,
                                            self.get_file_from_yaml()['input_buy_fund_info']['_amount_limit_text']).text
        return amount_limit_text

    # 用户测评的风险等级与基金风险等级不符时，会弹出提示
    @allure.step('取消提示')
    def cancel_alert(self):
        # if self.is_element_exist(element='confirm') == False:
        #     print("进入到确认购买页面")
        # else:
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_cancel_alert'])

    # 用户测评的风险等级与基金风险等级不符时，会弹出提示
    @allure.step('确认提示')
    def confirm_alert(self):
        # if self.is_element_exist(element='confirm') == False:
        #     print("进入到确认购买页面")
        # else:
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_confirm_alert'])

    # 认购基金时，会弹出提示信息“该基金目前处于认购状态，封闭期内不得赎回，继续交易？”
    @allure.step('确认认购提示')
    def confirm_subscribe_fund(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_confirm_subscribe'])

    # 认购基金时，会弹出提示信息“该基金目前处于认购状态，封闭期内不得赎回，继续交易？”
    @allure.step('取消认购提示')
    def cancel_subscribe_fund(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_cancel_subscribe'])

    @allure.step('点击关闭温馨提示')
    def click_close_warn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_confirm_btn'])

    @allure.step("获取最低投资金额")
    def get_lowest_amount(self):
        text = self.find_element(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_lowest_amount']).text
        lowest = self.get_numbers_from_str(text)
        return lowest[0]

    @allure.step('获取银行卡单笔限额')
    def get_bank_limit_amount(self):
        card_limit_text = self.find_element(By.ID, self.get_file_from_yaml()['input_buy_fund_info']['_card_limit']).text
        card_limit_amount = self.get_numbers_from_str(card_limit_text)
        return card_limit_amount[0]

    @allure.step("检查温馨提示是否存在")
    def check_tip_exist_or_not(self):
        status = self.is_element_exist(self.get_file_from_yaml()['input_buy_fund_info']['_warn'])
        return status

