import random
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.product_page import ProductPage


class TestRegisterAccount:

    register = PublicMethod()  # 创建对象
    register_mobile =  random.randint(13710000000, 13719999999)

    @allure.severity("critical")
    @allure.story("测试注册")
    @allure.title("注册账号")
    def test_register(self):
        self.register.setup(BasePage(self).get_data()['test_register']['_device_name'])
        self.register.agree_private_annce_skip_guide_page()
        ProductPage.go_to_mine_page(self.register.ll)
        LoginPage.register_account(self.register.ll)
        self.register.register_account(0, self.register_mobile, BasePage(self).get_data()['test_register']['_verify_code'],
                                       BasePage(self).get_data()['test_register']['_pwd'],
                                       BasePage(self).get_data()['test_register']['_confirm_pwd'])
        ProductPage.go_to_mine_page(self.register.ll)
        MinePage.click_trade_record(self.register.ll)
        MinePage.click_go_bind_card(self.register.ll)
        self.register.teardown()
