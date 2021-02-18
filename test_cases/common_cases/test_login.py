import time
import allure
from base.base_page import BasePage
from page.login_page import LoginPage
from page.public_methods import PublicMethod
from page.product_page import ProductPage


class TestLogin:

    login = PublicMethod()  # 创建对象

    @allure.severity("critical")
    @allure.story("测试登录")
    @allure.title("手机号，密码登录/登出")
    def test_login_and_logout(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        self.login.login_and_go_to_other_pages(BasePage(self).get_data()['test_login']['_mobile'],
                         BasePage(self).get_data()['test_login']['_pwd'], 0, 1)
        # with allure.step("断言:"):
        #     assert BasePage(self).get_data()['test_login']['_username'] == \
        #            MinePage.get_name(self.login.ll)
        self.login.logout(1)
        with allure.step("断言:"):
            assert ProductPage.get_product_btn_status(self.login.ll) == 'true'
        ProductPage.go_to_mine_page(self.login.ll)
        with allure.step("断言:"):
            assert LoginPage.get_forget_btn_text(self.login.ll) == BasePage(self).get_data()['test_login']['_forget_btn_text']
        self.login.teardown()
    #
    # @allure.severity("critical")
    # @allure.story("测试登录")
    # @allure.title("身份证号，密码登录")
    # def test_login_with_id_no(self):
    #     self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
    #     self.login.agree_private_annce_skip_guide_page(4)
    #     self.login.login(BasePage(self).get_data()['test_login']['_id_no'],
    #                      BasePage(self).get_data()['test_login']['_pwd'])
    #     time.sleep(2)
    #     with allure.step("断言:"):
    #         assert BasePage(self).get_data()['test_login']['_username'] == MinePage.get_username(self.login.ll)
    #     self.login.teardown()

    @allure.severity("normal")
    @allure.story("测试登录")
    @allure.title("不输入密码，登录按钮置灰")
    def test_login_without_pwd(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        LoginPage.input_username(self.login.ll, BasePage(self).get_data()['test_login']['_mobile'])
        with allure.step("断言:"):
            assert LoginPage.get_login_btn_status(self.login.ll) == 'false'
        self.login.teardown()

    @allure.severity("normal")
    @allure.story("测试登录")
    @allure.title("不输入账号，登录")
    def test_login_without_account(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        LoginPage.input_password(self.login.ll, BasePage(self).get_data()['test_login']['_pwd'])
        with allure.step("断言:"):
            assert LoginPage.get_login_btn_status(self.login.ll) == 'false'
        self.login.teardown()

    @allure.severity("normal")
    @allure.story("测试登录")
    @allure.title("输入错误账号，登录")
    def test_login_with_incorrect_account(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        self.login.login(BasePage(self).get_data()['test_login']['_incorrect_mobile'],
                         BasePage(self).get_data()['test_login']['_pwd'])
        time.sleep(1)
        with allure.step("断言:"):
            assert LoginPage.get_login_btn_status(self.login.ll) == 'false'
        self.login.teardown()

    @allure.severity("normal")
    @allure.story("测试登录")
    @allure.title("输入错误密码，登录")
    def test_login_with_incorrect_pwd(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        self.login.login(BasePage(self).get_data()['test_login']['_mobile'],
                         BasePage(self).get_data()['test_login']['_incorrect_pwd'])
        time.sleep(1)
        with allure.step("断言:"):
            assert BasePage(self).get_data()['test_login']['_toast_4'] == \
                   BasePage.get_toast(self.login.ll)
        self.login.teardown()

    @allure.severity("normal")
    @allure.story("测试登录")
    @allure.title("输入未注册手机号，登录")
    def test_login_with_unregister_account(self):
        self.login.setup(BasePage(self).get_data()['test_login']['_device_name'])
        self.login.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.login.ll)
        self.login.login(BasePage(self).get_data()['test_login']['_unregister_mobile'],
                         BasePage(self).get_data()['test_login']['_pwd'])
        time.sleep(1)
        with allure.step("断言:"):
            assert BasePage(self).get_data()['test_login']['_toast_5'] == \
                   BasePage.get_toast(self.login.ll)
        self.login.teardown()
