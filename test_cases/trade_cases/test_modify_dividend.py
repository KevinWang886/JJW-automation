import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.modify_dividend_page import ModifyDividendPage
from page.modify_dividend_success import ModifyDividendSuccess
from page.my_holding import MyHolding
from page.password import InputPassword
from page.product_page import ProductPage


class TestModifyDividend:

    modify_dividend = PublicMethod()
    trade_type = '029'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("修改分红方式")
    def test_modify_dividend(self):
        self.modify_dividend.setup(BasePage(self).get_data()['test_modify_dividend']['_device_name'])
        self.modify_dividend.agree_private_annce_skip_guide_page(1)
        self.modify_dividend.login_and_go_to_other_pages(BasePage(self).get_data()['test_modify_dividend']['_mobile'],
                                                BasePage(self).get_data()['test_modify_dividend']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.modify_dividend.ll)
        self.modify_dividend.fund_holding_details(4)
        ModifyDividendPage.select_dividend_method(self.modify_dividend.ll)
        ModifyDividendPage.click_confirm_btn(self.modify_dividend.ll)
        InputPassword.input_password(self.modify_dividend.ll)
        assert BasePage.get_data(self.modify_dividend.ll)['test_modify_dividend']['_success_text'] == \
               ModifyDividendSuccess.get_success_text(self.modify_dividend.ll)
