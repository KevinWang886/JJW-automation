import random
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.crs_page import CRSPage
from page.login_page import LoginPage
from page.register_success import RegisterSuccess


class TestRegisterOpenAccount:

    register = PublicMethod()
    mobile = '1370000'+str(random.randint(1000, 9999))
    id_no = '53010219940307'+str(random.randint(1000, 9999))
    card_no = '621700382919413'+str(random.randint(1000, 9999))

    @allure.severity("critical")
    @allure.story("注册开户")
    @allure.title("引导页，注册开户")
    def test_register_open_account(self):
        mobile = '1370000' + str(random.randint(1000, 9999))
        id_no = '53010219940307' + str(random.randint(1000, 9999))
        card_no = '621700382919413' + str(random.randint(1000, 9999))

        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        self.register.bind_card(BasePage(self).get_data()['test_register_open_account']['_name'], id_no, card_no,
                                mobile, BasePage(self).get_data()['test_register_open_account']['_verify_code_2'])
        self.register.set_trade_pwd(BasePage(self).get_data()['test_register_open_account']['_trade_pwd'],
                                    BasePage(self).get_data()['test_register_open_account']['_trade_pwd'])
        CRSPage.click_confirm_btn(self.register.ll)
        assert BasePage(self).get_data()['test_register_open_account']['_success_text'] == \
               RegisterSuccess.get_success_text(self.register.ll)

    @allure.severity("critical")
    @allure.story("注册开户")
    @allure.title("登录页面，注册用户")
    def test_register_account_from_login_page(self):
        mobile = '1370000' + str(random.randint(1000, 9999))
        id_no = '53010219940307' + str(random.randint(1000, 9999))
        card_no = '621700382919413' + str(random.randint(1000, 9999))

        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(4)
        LoginPage.click_register(self.register.ll)
        self.register.register_account(0, mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        self.register.bind_card(BasePage(self).get_data()['test_register_open_account']['_name'], id_no, card_no,
                                mobile, BasePage(self).get_data()['test_register_open_account']['_verify_code_2'])
        self.register.set_trade_pwd(BasePage(self).get_data()['test_register_open_account']['_trade_pwd'],
                                    BasePage(self).get_data()['test_register_open_account']['_trade_pwd'])
        CRSPage.click_confirm_btn(self.register.ll)
        assert BasePage(self).get_data()['test_register_open_account']['_success_text'] == \
               RegisterSuccess.get_success_text(self.register.ll)

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("用户已经注册")
    def test_already_registered(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, BasePage(self).get_data()['test_register_open_account']['_registered_mobile'],
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_10']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，不输入手机号，注册")
    def test_register_account_without_mobile(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(tag=1, mobile=None,
                                       verify_code=BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       pwd=BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       confirm_pwd=BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_1']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，不输入验证码，注册")
    def test_register_account_without_verify_code(self):

        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(2, self.mobile, None,
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_2']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，不输入登录密码，注册")
    def test_register_account_without_pwd(self):

        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(3, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'], None,
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_3']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，不输入确认登录密码，注册")
    def test_register_account_without_confirm_pwd(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(4, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'], None)
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_4']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，手机号输入错误")
    def test_register_account_with_incorrect_mobile(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, BasePage(self).get_data()['test_register_open_account']['_short_mobile'],
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_5']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，输入验证位数错误")
    def test_register_account_with_short_verify_code(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_short_verify_code'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_6']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，输入登录密码错误")
    def test_register_account_with_short_pwd(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_short_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_7']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，两次密码不一致")
    def test_register_account_with_different_pwd(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_verify_code_1'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_different_confirm_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_8']
        self.register.teardown()

    @allure.severity("normal")
    @allure.story("注册开户")
    @allure.title("引导页，输入错误验证按")
    def test_register_account_incorrect_verify_code(self):
        self.register.setup(BasePage(self).get_data()['test_register_open_account']['_device_name'])
        self.register.swap_guide_and_go_to_different_pages(1)
        self.register.register_account(0, self.mobile,
                                       BasePage(self).get_data()['test_register_open_account']['_incorrect_verify_code'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'],
                                       BasePage(self).get_data()['test_register_open_account']['_login_pwd'])
        assert BasePage.get_toast(self.register.ll) == \
               BasePage(self).get_data()['test_register_open_account']['_registered_error_9']
        self.register.teardown()

