import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class BindCard(BasePage):

    @allure.step("输入姓名")
    def input_name(self, name):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card']['_name'], name)

    @allure.step("输入身份证号")
    def input_id_card_no(self, id_card_no):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card']['_id_card_no'], id_card_no)

    @allure.step("点击有效期")
    def click_valid_date(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_valid_date'])

    @allure.step("选择长期有效")
    def select_long_time(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_long_time'])

    @allure.step("输入银行卡号")
    def input_card_no(self, card_no):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card']['_bank_card_no'], card_no)

    @allure.step("选择开户行")
    def click_open_bank(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_bank'])

    @allure.step("选择建行")
    def select_bank(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['bind_card']['_bank_name'])

    @allure.step("选择联系地址")
    def click_address(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_address'])

    @allure.step("选择城市")
    def click_city(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_select_city'])

    @allure.step("选择省份")
    def select_province(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['bind_card']['_province'])

    @allure.step("选择市")
    def select_city(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['bind_card']['_city'])

    @allure.step("点击保存联系地址")
    def click_save(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_save_btn'])

    @allure.step("点击职业")
    def click_professor(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_professor'])

    @allure.step("点击确定保存职业")
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_confirm_btn'])

    @allure.step("输入手机号")
    def input_mobile_no(self, mobile):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card']['_mobile'], mobile)

    @allure.step("获取验证码")
    def get_verify_code(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_send_code'])

    @allure.step("输入验证码")
    def input_verify_code(self, verify_code):
        self.send_keys(By.ID, self.get_file_from_yaml()['bind_card']['_verify_code'], verify_code)

    @allure.step("点击下一步按钮")
    def click_next_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['bind_card']['_next_btn'])








