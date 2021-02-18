from base.base_page import BasePage
from page.public_methods import PublicMethod
import allure


class TestTradeRecords:

    trade_records = PublicMethod()

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("交易类型查询")
    def test_trade_records_type(self):
        self.trade_records.setup(BasePage(self).get_data()['test_trade_records']['_device_name'])
        self.trade_records.agree_private_annce_skip_guide_page(1)
        self.trade_records.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_records']['_mobile'],
                                                     BasePage(self).get_data()['test_trade_records']['_pwd'],
                                                     0, 6)
        for i in range(0, 2):
            self.trade_records.trade_records(action="交易类型", tag=i)
        for j in range(0, 3):
            self.trade_records.trade_records(action="交易状态", tag=j)

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("交易状态查询")
    def test_trade_records_status(self):
        self.trade_records.setup(BasePage(self).get_data()['test_trade_records']['_device_name'])
        self.trade_records.agree_private_annce_skip_guide_page(1)
        self.trade_records.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_records']['_mobile'],
                                                     BasePage(self).get_data()['test_trade_records']['_pwd'],
                                                     0, 6)
        for i in range(0, 3):
            self.trade_records.trade_records(action="交易状态", tag=i)


