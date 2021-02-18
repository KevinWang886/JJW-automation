import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class MinePage(BasePage):

    @allure.step("我的页面，进入产品页")
    def go_to_product_page(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_main_menu'])

    @allure.step("我的页面，进入名人堂页")
    def go_to_famous_page(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_famous_menu'])

    @allure.step("我的页面，进入驾驶室页面")
    def go_to_driver_menu(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_driver_menu'])

    @allure.step("我的页面，进入账户管理页")
    def go_to_account_management(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_account_management'])

    @allure.step("我的页面，获取用户手机号")
    def get_mobile(self):
        mobile = self.find_element(By.ID, self.get_file_from_yaml()['mine_page']['_mobile']).text
        return mobile

    @allure.step("我的页面，获取用户姓名")
    def get_name(self):
        name = self.find_element(By.ID, self.get_file_from_yaml()['mine_page']['_name']).text
        return name

    @allure.step("我的页面，点击创建组合")
    def click_create_group(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_create_group'])

    @allure.step("点击【去绑卡】")
    def click_go_bind_card(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_go_bind_card'])

    @allure.step("点击【取消】绑卡")
    def click_cancel_bind_card(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_cancel_bind_card'])

    @allure.step("我的页面，点击交易记录")
    def click_my_assert(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_my_assert'])

    @allure.step("我的页面，点击交易记录")
    def click_trade_record(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_trade_record'])

    @allure.step("我的页面，点击我的资产")
    def click_my_asserts(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_my_asserts'])

    @allure.step("我的页面，点击基金定投")
    def click_fix_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_fix_buy'])

    @allure.step("我的页面，点击分红明细")
    def click_devidened_details(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_dividened'])

    @allure.step("我的页面，点击我的打赏/关注")
    def click_my_focus(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_my_subscribe'])

    @allure.step("我的页面，点击我的自选")
    def click_my_selected(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_my_selected'])

    @allure.step("我的页面，点击分享邀请")
    def click_share(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_share'])

    @allure.step("我的页面，点击我的金基币")
    def click_my_mall(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_my_mall'])

    @allure.step("我的页面，点击金基币活动页")
    def click_activity(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['mine_page']['_activity_linearlayout'])

    @allure.step("我的页面，获取用户积分")
    def get_point(self):
        point = self.find_element(By.ID, self.get_file_from_yaml()['mine_page']['point_tv']).text
        return point

