from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.my_holding import HoldDetails
from page.trade_query_page import TradeQueryPage


class TestTradeQuery:

    trade_query = PublicMethod()

    def test_hold_details(self):
        self.trade_query.setup(BasePage(self).get_data()['test_trade_query']['_device_name'])
        self.trade_query.swap_guide_and_go_to_different_pages(4)
        self.trade_query.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_query']['_mobile'],
                                                     BasePage(self).get_data()['test_trade_query']['_pwd'],
                                                     tag=9)
        TradeQueryPage.click_trade_details(self.trade_query.ll)
        assert int(HoldDetails.get_fund_count(self.trade_query.ll)) == HoldDetails.get_hold_fund(self.trade_query.ll)
        assert float(HoldDetails.get_total_income(self.trade_query.ll)) == self.trade_query.total_income()
        assert HoldDetails.get_total_value(self.trade_query.ll) == self.trade_query.total_market_value()

