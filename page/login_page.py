import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("输入用户名")
    def input_username(self, username):  # 登录输入手机号和密码
        self.send_keys(By.ID, self.get_file_from_yaml()['login']['_account'], username)

    @allure.step("输入登录密码")
    def input_password(self, password):
        self.send_keys(By.ID, self.get_file_from_yaml()['login']['_password'], password)

    @allure.step("点【登录按钮】")
    def login_btn(self):   # 登录按钮
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_login'])

    @allure.step("获取【登录按钮】的状态")
    def get_login_btn_status(self):   # 登录按钮
        login_btn_status = self.find_element(By.ID,
                                                self.get_file_from_yaml()['login']['_login']).get_attribute("enabled")
        return login_btn_status

    @allure.step("取消开启手势密码")
    def cancel_gesture(self):  # 取消开启手势密码
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_cancel'])

    @allure.step("获取开启手势密码提示内容")
    def open_gesture_or_not(self):  # 获取开启手势密码提示内容
        gesture_alter = self.find_element(By.ID, self.get_file_from_yaml()['login']['_gesture']).text
        return gesture_alter

    @allure.step("进入到首页")
    def go_to_menu_page(self):  # 进入到首页
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_menu_button'])

    @allure.step("开启手势密码")
    def confirm_gesture(self):  # 开启手势密码
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_confirm'])

    @allure.step("我的持仓")
    def my_fund(self):  # 我的持仓
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_my_fund_locator'])

    @allure.step("注册账号")
    def register_account(self):
        self.find_element_and_click(By.ID,  self.get_file_from_yaml()['login']['_register_account'])

    @allure.step("点击【驾驶室】")
    def go_to_product_page(self):  # 点击【驾驶室】去驾驶室页面
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_product_page'])

    @allure.step("未登录时我的页面，获取忘记密码的内容")
    def get_forget_btn_text(self):   # 获取忘记密码的内容
        reset_btn_text = self.find_element(By.ID, self.get_file_from_yaml()['login']['_forget_btn']).text
        return reset_btn_text

    @allure.step("未登录时我的页面，进入忘记密码页面")
    def click_forget_pwd_btn(self):   # 进入忘记密码页面
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['login']['_forget_btn'])

