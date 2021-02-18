import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TradeRecordsPage(BasePage):

    @allure.step("点击交易类型")
    def click_trade_type(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_records_page']['_trade_type'])

    @allure.step("点击交易时间")
    def click_trade_time(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_records_page']['_trade_date'])

    @allure.step("点击交易状态")
    def click_trade_status(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['trade_records_page']['_trade_status'])

    @allure.step("选择全部")
    def select_all(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_all'])

    @allure.step("选择认购")
    def select_subscribe(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_subscribe'])

    @allure.step("选择申购")
    def select_buy(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_buy'])

    @allure.step("选择赎回")
    def select_redeem(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_redeem'])

    @allure.step("选择转换")
    def select_transfer(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_transfer'])

    @allure.step("选择强赎")
    def force_redeem(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_force_redeem'])

    @allure.step("选择定投")
    def select_fix(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_fix'])

    @allure.step("选择强增")
    def force_add(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_force_add'])

    @allure.step("选择强减")
    def force_cut(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_force_cut'])

    @allure.step("选择近一个月")
    def select_one_month(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_one_month'])

    @allure.step("选择三个月")
    def select_three_months(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_three_months'])

    @allure.step("选择一年")
    def select_one_year(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_one_year'])

    @allure.step("选择确认失败")
    def select_confirm_fail(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_confirm_fail'])

    @allure.step("选择确认中")
    def select_confirming(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_confirming'])

    @allure.step("选择确认成功")
    def select_confirm_success(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_confirm_success'])

    @allure.step("选择交易失败")
    def select_trade_fail(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_trade_fail'])

    @allure.step("选择已撤单")
    def select_undo(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_undo'])

    @allure.step("点击交易记录")
    def click_trade_record(self):
        trade_records = self.find_elements(By.XPATH, self.get_file_from_yaml()['trade_records_page']['_trade_record'])
        if len(trade_records) > 0:
            trade_records[0].click()
        else:
            self.log.info("no trade record")

    @allure.step("获取交易记录状态")
    def get_record_state(self):
        # if BasePage.is_element_exist(self, self.get_file_from_yaml()['trade_records_page']['_trans_state_text']):
        record_state = self.find_elements(By.ID, self.get_file_from_yaml()['trade_records_page']['_trans_state_text'])
        if len(record_state) > 0:
            return record_state[0].text
        else:
            self.log.info("no trade record")
        # return record_state[0].text
        # else:
        #     self.log.info("no trade record")

    @allure.step("获取交易记录类型")
    def get_record_type(self):
        # if BasePage.is_element_exist(self, self.get_file_from_yaml()['trade_records_page']['_trade_type_text']):
        record_type = self.find_elements(By.ID, self.get_file_from_yaml()['trade_records_page']['_trade_type_text'])
        if len(record_type) > 0:
            return record_type[0].text
        else:
            self.log.info("no trade record")
        # else:
        #     self.log.info("no trade record")
