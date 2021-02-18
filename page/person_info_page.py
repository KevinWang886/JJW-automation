import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PersonInfo(BasePage):

    @allure.step('点击职业')
    def click_professional(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_professional'])

    @allure.step('获取当前职业')
    def get_current_professor(self):
        current_professor = \
            self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_professional_text']).text
        return current_professor

    @allure.step('点击婚姻状态')
    def click_marriage_status(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_marriage_status'])

    @allure.step('获取当前婚姻状态')
    def get_current_marriage_status(self):
        current_marriage_status = \
            self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_marriage_text']).text
        return current_marriage_status

    @allure.step('点击学历')
    def click_education(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_education'])

    @allure.step('获取当前学历')
    def get_current_education(self):
        current_education = \
            self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_education_text']).text
        return current_education

    @allure.step('点击年收入')
    def click_annual_income(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_annual_income'])

    @allure.step('获取当前年收入')
    def get_current_annual_income(self):
        current_annual_income = \
            self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_annual_income_text']).text
        return current_annual_income

    @allure.step('向下滑动滑块')  # 字典：2学历，3年收入，4婚姻状态， 5职业
    def slip_up_or_down(self, flag):
        if flag == 1:
            if PersonInfo.get_current_education(self) == '初中以下':
                PersonInfo.click_education(self)
                self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
            else:
                PersonInfo.click_education(self)
                self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
        elif flag == 2:
            if PersonInfo.get_current_annual_income(self) == '1万以下':
                PersonInfo.click_annual_income(self)
                self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
            else:
                PersonInfo.click_education(self)
                self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
        elif flag == 3:
            if PersonInfo.get_current_marriage_status(self) == '未婚':
                PersonInfo.click_marriage_status(self)
                self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
            else:
                PersonInfo.click_education(self)
                self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
        elif flag == 4:
            if PersonInfo.get_current_professor(self) == '政府部门':
                PersonInfo.click_professional(self)
                self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
            else:
                PersonInfo.click_education(self)
                self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_picker'])
        PersonInfo.click_confirm_btn(self)

    @allure.step('点击取消按钮')
    def click_cancel_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_cancel'])

    @allure.step('点击确定按钮')
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_confirm'])

    @allure.step('点击提交按钮')
    def click_submit_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_submit'])



    # @allure.step('获取当前职业')
    # def get_current_professor(self):
    #     current_professor = \
    #         self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_professional_text']).text
    #     return current_professor
    #
    # @allure.step('点击职业')
    # def click_professor(self):
    #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_professor'])
    #
    # @allure.step('选择职业，向下滑动')
    # def select_professor_down(self):
    #     self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_professor_picker'])
    #
    # @allure.step('选择职业，向上滑动')
    # def select_professor_up(self):
    #     self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_professor_picker'])

    # @allure.step('获取当前学历')
    # def get_current_education(self):
    #     current_education = \
    #         self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_current_education']).text
    #     return current_education
    #
    # @allure.step('点击学历')
    # def click_education(self):
    #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_education'])
    #
    # @allure.step('选择学历，上划')
    # def select_education_up(self):
    #     self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_education_picker'])
    #
    # @allure.step('选择下划')
    # def select_education_down(self):
    #     self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_education_picker'])
    #
    # @allure.step('获取当前年收入')
    # def get_current_annual_income(self):
    #     current_annual_income = \
    #         self.find_element(By.ID, self.get_file_from_yaml()['person_info_page']['_current_annual_income']).text
    #     return current_annual_income
    #
    # @allure.step('点击年收入')
    # def click_annual_income(self):
    #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_annual_income'])
    #
    # @allure.step('选择年收入，上划')
    # def select_annual_income_up(self):
    #     self.slip_control_btn_up(By.ID, self.get_file_from_yaml()['person_info_page']['_annual_income_picker'])
    #
    # @allure.step('选择年收入，下滑')
    # def select_annual_income_down(self):
    #     self.slip_control_btn_down(By.ID, self.get_file_from_yaml()['person_info_page']['_annual_income_picker'])
    #
    # @allure.step('点击‘提交')
    # def click_submit_btn(self):
    #     self.find_element_and_click(By.ID, self.get_file_from_yaml()['person_info_page']['_submit_btn'])











