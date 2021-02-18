import random
import allure
from base.base_page import BasePage
from page.Input_buy_fund_info import InputBuyFundInfo
from page.public_methods import PublicMethod
from page.buy_fund_success import BuyFundSuccess


class TestBuyFund:

    buy_fund = PublicMethod()
    amount = random.randint(100, 199)

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("申购基金")
    def test_buy_fund(self):
        self.buy_fund.setup(BasePage(self).get_data()['test_buy_fund']['_device_name'])
        self.buy_fund.agree_private_annce_skip_guide_page(1)
        self.buy_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_buy_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_buy_fund']['_pwd'],
                                                  0, 2)
        self.buy_fund.search_and_click(BasePage(self).get_data()['test_buy_fund']['_fund_code'])
        self.buy_fund.fund_info(0)
        self.buy_fund.input_buy_info(self.amount)
        assert BasePage(self).get_data()['test_buy_fund']['_success_text'] == \
               BuyFundSuccess.get_success_text(self.buy_fund.ll)
        self.buy_fund.teardown()

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("未输入购买金额")
    def test_not_input_amount(self):
        self.buy_fund.setup(BasePage(self).get_data()['test_buy_fund']['_device_name'])
        self.buy_fund.agree_private_annce_skip_guide_page(1)
        self.buy_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_buy_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_buy_fund']['_pwd'],
                                                  0, 2)
        self.buy_fund.search_and_click(BasePage(self).get_data()['test_buy_fund']['_fund_code'])
        self.buy_fund.fund_info(0)
        self.buy_fund.opposite_actions_in_buy_fund(tag=0)
        self.buy_fund.teardown()

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("未勾选协议")
    def test_not_input_amount(self):
        self.buy_fund.setup(BasePage(self).get_data()['test_buy_fund']['_device_name'])
        self.buy_fund.agree_private_annce_skip_guide_page(1)
        self.buy_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_buy_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_buy_fund']['_pwd'],
                                                  0, 2)
        self.buy_fund.search_and_click(BasePage(self).get_data()['test_buy_fund']['_fund_code'])
        self.buy_fund.fund_info(0)
        self.buy_fund.opposite_actions_in_buy_fund(tag=1)
        self.buy_fund.teardown()

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("购买金额超过银行卡单笔限额")
    def test_larger_than_card_limit(self):
        self.buy_fund.setup(BasePage(self).get_data()['test_buy_fund']['_device_name'])
        self.buy_fund.agree_private_annce_skip_guide_page(1)
        self.buy_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_buy_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_buy_fund']['_pwd'],
                                                  0, 2)
        self.buy_fund.search_and_click(BasePage(self).get_data()['test_buy_fund']['_fund_code'])
        self.buy_fund.fund_info(0)
        self.buy_fund.opposite_actions_in_buy_fund(tag=2)
        assert InputBuyFundInfo.get_amount_limit_text(self.buy_fund.ll) == \
               BasePage(self).get_data()['test_buy_fund']['_larger_than_bank_limit']

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("输入购买金额小于起投金额")
    def test_larger_than_card_limit(self):
        self.buy_fund.setup(BasePage(self).get_data()['test_buy_fund']['_device_name'])
        self.buy_fund.agree_private_annce_skip_guide_page(1)
        self.buy_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_buy_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_buy_fund']['_pwd'],
                                                  0, 2)
        self.buy_fund.search_and_click(BasePage(self).get_data()['test_buy_fund']['_fund_code'])
        self.buy_fund.fund_info(0)
        self.buy_fund.opposite_actions_in_buy_fund(tag=3)







