import random
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.Input_buy_fund_info import InputBuyFundInfo
from page.buy_fund_success import BuyFundSuccess
from page.confirm_buy_info import ConfirmBuyInfo
from page.fund_info import FundInfo
from page.home_page import HomePage


class TestSubscribeFund:

    subscribe_fund = PublicMethod()
    amount = random.randint(1000, 1199)
    trade_type = '020'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("认购基金")
    def test_buy_fund(self):
        self.subscribe_fund.setup(BasePage(self).get_data()['test_subscribe_fund']['_device_name'])
        self.subscribe_fund.swap_guide_and_go_to_different_pages(4)
        self.subscribe_fund.login_and_go_to_other_pages(BasePage(self).get_data()['test_subscribe_fund']['_mobile'],
                                                  BasePage(self).get_data()['test_subscribe_fund']['_pwd'], tag=6)
        HomePage.click_search_btn(self.subscribe_fund.ll)
        self.subscribe_fund.search_and_click(BasePage(self).get_data()['test_subscribe_fund']['_fund_code'])
        FundInfo.click_buy_now(self.subscribe_fund.ll)
        self.subscribe_fund.input_buy_info(self.amount)
        InputBuyFundInfo.confirm_subscribe_fund(self.subscribe_fund.ll)
        assert float(ConfirmBuyInfo.get_balance(self.subscribe_fund.ll)) == float(self.amount)
        self.subscribe_fund.confirm_and_input_pwd(trade_type=self.trade_type)
        assert BasePage(self).get_data()['test_subscribe_fund']['_success_text'] == \
               BuyFundSuccess.get_success_text(self.subscribe_fund.ll)
        self.subscribe_fund.teardown()
