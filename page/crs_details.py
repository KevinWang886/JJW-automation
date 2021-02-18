import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CRSDetails(BasePage):

    @allure.step("输入姓")
    def input_lastname(self, lastname):
        self.send_keys(By.ID, self.get_file_from_yaml()['crs_details']['_lastname'], lastname)

    @allure.step("获取姓")
    def get_lastname(self):
        lastname = self.find_element(By.ID, self.get_file_from_yaml()['crs_details']['_lastname']).text
        return lastname

    @allure.step("输入名")
    def input_firstname(self, input_firstname):
        self.send_keys(By.ID, self.get_file_from_yaml()['crs_details']['_firstname'], input_firstname)

    @allure.step("获取名")
    def get_firstname(self):
        firstname = self.find_element(By.ID, self.get_file_from_yaml()['crs_details']['_firstname']).text
        return firstname

    @allure.step("输入居住地")
    def input_live_address(self, live_address):
        self.send_keys(By.ID, self.get_file_from_yaml()['crs_details']['_live_address'], live_address)

    @allure.step("输入出生地")
    def input_birth_address(self, birth_address):
        self.send_keys(By.ID, self.get_file_from_yaml()['crs_details']['_birth_address'], birth_address)

    @allure.step("输入纳税号")
    def input_tax_number(self, tax_number):
        self.send_keys(By.ID, self.get_file_from_yaml()['crs_details']['_tax_number'], tax_number)

    @allure.step("选择性别")
    def select_gender(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_gender'])
        CRSDetails.click_confirm(self)

    @allure.step("选择生日")
    def select_birthday(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_birthday'])
        self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['crs_details']['_year'])
        self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['crs_details']['_month'])
        self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['crs_details']['_day'])
        CRSDetails.click_confirm(self)

    @allure.step("选择居住国家")
    def select_live_country(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_live_country'])
        CRSDetails.click_confirm(self)

    @allure.step("选择出生国家")
    def select_birth_country(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_birth_country'])
        CRSDetails.click_confirm(self)

    @allure.step("选择税收居民国")
    def select_tax_country(self):
        tax_country = self.find_elements(By.ID, self.get_file_from_yaml()['crs_details']['_tax_country'])
        if len(tax_country) == 1:
            tax_country[0].click()
            self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['crs_details']['_picker'])
        elif len(tax_country) == 2:
            tax_country[1].click()
            self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['crs_details']['_picker'])
        CRSDetails.click_confirm(self)

    @allure.step("选择无纳税人识别号原因")
    def select_tax_reason(self):
        tax_reason = self.find_elements(By.ID, self.get_file_from_yaml()['crs_details']['_tax_reason'])
        if len(tax_reason) == 1:
            tax_reason[0].click()
        elif len(tax_reason) == 2:
            tax_reason[1].click()
        CRSDetails.click_confirm(self)

    @allure.step("新增税收国")
    def click_add_tax_country(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_add_tax'])

    @allure.step("删除税收国")
    def click_delete_tax_country(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_delete_tax'])

    @allure.step("点击【确定】")
    def click_confirm(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_confirm'])

    @allure.step("点击【提交资料】")
    def click_submit_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['crs_details']['_submit_btn'])
