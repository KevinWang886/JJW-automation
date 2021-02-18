import random
import time
import allure
from base.base_page import BasePage
from page.account_management_page import AccountManagementPage
from page.add_card_page import AddCardPage
from page.public_methods import PublicMethod
from page.crs_details import CRSDetails
from page.crs_page import CRSPage
from page.login_page import LoginPage
from page.product_page import ProductPage
from page.reset_pwd_page import ResetPwdPage


class TestAccountManagement:

    acc_mng = PublicMethod()  # 创建对象

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("重置登录密码")
    def test_reset_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_reset_pwd(self.acc_mng.ll)
        self.acc_mng.reset_pwd(BasePage(self).get_data()['test_account_management']['_mobile'],
                               BasePage(self).get_data()['test_account_management']['_verify_code_1'],
                               BasePage(self).get_data()['test_account_management']['_new_pwd'],
                               BasePage(self).get_data()['test_account_management']['_new_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_toast_text'] == \
               BasePage.get_toast(self.acc_mng.ll)
        self.acc_mng.teardown()

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("未登录忘记登录密码")
    def test_reset_pwd_without_login(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.agree_private_annce_skip_guide_page()
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_username'],
                                         BasePage(self).get_data()['test_account_management']['_password'],
                                         0,1)
        self.acc_mng.reset_pwd(BasePage(self).get_data()['test_account_management']['_mobile'],
                               BasePage(self).get_data()['test_account_management']['_verify_code_1'],
                               BasePage(self).get_data()['test_account_management']['_new_pwd'],
                               BasePage(self).get_data()['test_account_management']['_new_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_toast_text'] == \
               BasePage.get_toast(self.acc_mng.ll)
        self.acc_mng.teardown()

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("未登录忘记密码，输入未注册账号")
    def test_forget_pwd_input_unregister_account(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.agree_private_annce_skip_guide_page(4)
        LoginPage.click_forget_pwd(self.acc_mng.ll)
        ResetPwdPage.input_mobile(self.acc_mng.ll,
                                  BasePage(self).get_data()['test_account_management']['_unregister_mobile'])
        ResetPwdPage.get_code(self.acc_mng.ll)
        assert BasePage(self).get_data()['test_account_management']['_toast_text_3'] == \
               BasePage.get_toast(self.acc_mng.ll)
        self.acc_mng.teardown()

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("重置交易密码")
    def test_reset_trade_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_reset_trade_pwd(self.acc_mng.ll)
        self.acc_mng.reset_trade_pwd(BasePage(self).get_data()['test_account_management']['_id_no'],
                                     BasePage(self).get_data()['test_account_management']['_name'],
                                     BasePage(self).get_data()['test_account_management']['_mobile'],
                                     BasePage(self).get_data()['test_account_management']['_verify_code_1'],
                                     BasePage(self).get_data()['test_account_management']['_new_trade_pwd'],
                                     BasePage(self).get_data()['test_account_management']['_new_trade_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_toast_text_2'] == \
               BasePage.get_toast(self.acc_mng.ll)
        self.acc_mng.teardown()

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("修改个人资料")
    def test_modify_person_info(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.acc_mng.ll)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_username'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'],
                                                 0, 1)
        AccountManagementPage.click_personal_info(self.acc_mng.ll)
        self.acc_mng.modify_personal_info()
        # assert BasePage.get_toast(self.acc_mng.ll) == \
        #        BasePage(self).get_data()['test_account_management']['_toast_text_2']
        # self.acc_mng.teardown()

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("测试新增银行卡")
    def test_bind_bank_card(self):
        card_no = '621700803611140'+str(random.randint(1000, 9999))
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile_no'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_bank_card(self.acc_mng.ll)
        self.acc_mng.add_bank_card(card_no,
                                   BasePage(self).get_data()['test_account_management']['_mobile'],
                                   BasePage(self).get_data()['test_account_management']['_verify_code_2'],
                                   BasePage(self).get_data()['test_account_management']['_trade_pwd'])
        time.sleep(2)
        assert AddCardPage.get_card_name(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_bank_name']
        assert AddCardPage.get_card_status(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_bank_status']

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱")
    def test_modify_email(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(0, BasePage(self).get_data()['test_account_management']['_correct_email'],
                                  BasePage(self).get_data()['test_account_management']['_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_modify_email_success_toast'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱,不输入新邮箱和密码")
    def test_modify_email_without_email_and_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(3, None, None)
        assert BasePage(self).get_data()['test_account_management']['_modify_email_error_1'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱,输入错误格式邮箱")
    def test_modify_email_with_incorrect_email(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(0, BasePage(self).get_data()['test_account_management']['_incorrect_email'],
                                  BasePage(self).get_data()['test_account_management']['_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_modify_email_error_2'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱,不输入登录密码")
    def test_modify_email_without_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(2, BasePage(self).get_data()['test_account_management']['_correct_email'], None)
        assert BasePage(self).get_data()['test_account_management']['_modify_email_error_3'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱,输入登录密码位数不足")
    def test_modify_email_with_short_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(0, BasePage(self).get_data()['test_account_management']['_correct_email'],
                                  BasePage(self).get_data()['test_account_management']['_short_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_modify_email_error_4'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改邮箱,输入错误登录密码")
    def test_modify_email_with_incorrect_pwd(self):
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_email(self.acc_mng.ll)
        self.acc_mng.modify_email(0, BasePage(self).get_data()['test_account_management']['_correct_email'],
                                  BasePage(self).get_data()['test_account_management']['_incorrect_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_modify_email_error_5'] == \
               BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("critical")
    @allure.story("测试账户管理")
    @allure.title("修改手机号")
    def test_modify_mobile(self):
        new_mobile = '136'+str(random.randint(10000000, 99999999))
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_current_mobile'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag=1)
        AccountManagementPage.click_mobile(self.acc_mng.ll)
        self.acc_mng.modify_mobile(BasePage(self).get_data()['test_account_management']['_id_no_2'],
                                   BasePage(self).get_data()['test_account_management']['_name_2'],
                                   BasePage(self).get_data()['test_account_management']['_current_mobile'], new_mobile,
                                   BasePage(self).get_data()['test_account_management']['_verify_code_1'],
                                   BasePage(self).get_data()['test_account_management']['_trade_pwd'])
        assert BasePage(self).get_data()['test_account_management']['_toast_text'] == BasePage.get_toast(self.acc_mng.ll)

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改CRS为非中国")
    def test_modify_crs_not_chinese(self):
        tag = 1
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile_1'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], tag)
        self.acc_mng.go_to_different_crs_page(tag)
        self.acc_mng.crs_details(BasePage(self).get_data()['test_account_management']['_lastname'],
                                 BasePage(self).get_data()['test_account_management']['_firstname'],
                                 BasePage(self).get_data()['test_account_management']['_live_address'],
                                 BasePage(self).get_data()['test_account_management']['_birth_address'],
                                 BasePage(self).get_data()['test_account_management']['_tax_number'], tag)
        self.acc_mng.click_return_btn()
        AccountManagementPage.click_crs(self.acc_mng.ll)
        assert CRSPage.get_not_china_status(self.acc_mng.ll) == 'true'
        CRSPage.click_confirm_btn(self.acc_mng.ll)
        assert CRSDetails.get_lastname(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_lastname']
        assert CRSDetails.get_firstname(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_firstname']

    @allure.severity("normal")
    @allure.story("测试账户管理")
    @allure.title("修改CRS既为中国又为其他国家或地区")
    def test_modify_crs_not_chinese(self):
        tag = 2
        self.acc_mng.setup(BasePage(self).get_data()['test_account_management']['_device_name'])
        self.acc_mng.swap_guide_and_go_to_different_pages(4)
        self.acc_mng.login_and_go_to_other_pages(BasePage(self).get_data()['test_account_management']['_mobile_1'],
                                                 BasePage(self).get_data()['test_account_management']['_pwd'], 1)
        self.acc_mng.go_to_different_crs_page(tag)
        self.acc_mng.crs_details(BasePage(self).get_data()['test_account_management']['_lastname'],
                                 BasePage(self).get_data()['test_account_management']['_firstname'],
                                 BasePage(self).get_data()['test_account_management']['_live_address'],
                                 BasePage(self).get_data()['test_account_management']['_birth_address'],
                                 BasePage(self).get_data()['test_account_management']['_tax_number'], tag)
        self.acc_mng.click_return_btn()
        # AccountManagementPage.click_crs(self.acc_mng.ll)
        assert CRSPage.get_all_status(self.acc_mng.ll) == 'true'
        CRSPage.click_confirm_btn(self.acc_mng.ll)
        assert CRSDetails.get_lastname(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_lastname']
        assert CRSDetails.get_firstname(self.acc_mng.ll) == \
               BasePage(self).get_data()['test_account_management']['_firstname']
