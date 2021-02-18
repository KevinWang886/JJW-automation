import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TradeApplyRecords(BasePage):

    @allure.step("点击交易类型")
    def click_trade_type(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_apply_records']['_trade_type'])

    @allure.step("点击交易时间")
    def click_trade_time(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_apply_records']['_trade_time'])

    @allure.step("选择全部")
    def select_all(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_all'])

    @allure.step("选择认购")
    def select_subscribe(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_subscribe'])

    @allure.step("选择申购")
    def select_buy(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_buy'])

    @allure.step("选择赎回")
    def select_redeem(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_redeem'])

    @allure.step("选择转换")
    def select_transfer(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_transfer'])

    @allure.step("选择撤单")
    def select_undo(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_undo'])

    @allure.step("选择定投")
    def select_fix(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_fix'])

    @allure.step("选择修改分红方式")
    def select_modify_dividend(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_modify_dividend'])

    @allure.step("选择近一个月")
    def select_one_month(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_one_month'])

    @allure.step("选择三个月")
    def select_three_months(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_three_months'])

    @allure.step("选择一年")
    def select_one_year(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_apply_records']['_one_year'])

    @allure.step("点击交易记录")
    def click_trade_record(self):
        trade_record = self.find_elements(By.ID, self.get_file_from_yaml()['trade_apply_records']['_trade_record'])
        if len(trade_record) > 0:
            trade_record[0].click()
        else:
            self.log.info("no trade record")

    @allure.step("获取交易记录状态")
    def get_record_state(self):
        record_state = self.find_elements(By.ID, self.get_file_from_yaml()['trade_apply_records']['_state'])
        return record_state[0].text
