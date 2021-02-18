import time
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.trade_records_page import TradeApplyRecords
from page.trade_record_details import TradeRecordDetails


class TestTradeRecords:

    trade_record = PublicMethod()

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金申购申请交易记录")
    def test_buy_fund_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='申购')
        time.sleep(5)
        if TradeApplyRecords.get_record_state(self.trade_record.ll) == '确认中':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '确认中'
        elif TradeApplyRecords.get_record_state(self.trade_record.ll) == '撤单':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '撤单'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '申购'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '指数型'

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金认购申请交易记录")
    def test_subscribe_fund_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='认购')
        time.sleep(5)
        TradeApplyRecords.click_trade_record(self.trade_record.ll)
        assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '确认中'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '认购'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '股票型'

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金赎回申请交易记录")
    def test_redeem_fund_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile_1'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd_1'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='赎回')
        time.sleep(5)
        if TradeApplyRecords.get_record_state(self.trade_record.ll) == '确认中':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '确认中'
        elif TradeApplyRecords.get_record_state(self.trade_record.ll) == '撤单':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '撤单'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '赎回'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '指数型'

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金转换申请交易记录")
    def test_transfer_fund_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile_1'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd_1'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='转换')
        time.sleep(5)
        if TradeApplyRecords.get_record_state(self.trade_record.ll) == '确认中':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '确认中'
        elif TradeApplyRecords.get_record_state(self.trade_record.ll) == '撤单':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '撤单'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '转换'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '指数型'

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金撤单申请交易记录")
    def test_undo_fund_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile_1'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd_1'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='撤单')
        time.sleep(5)
        TradeApplyRecords.click_trade_record(self.trade_record.ll)
        assert TradeRecordDetails.get_trade_status(self.trade_record.ll) == '确认成功'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '撤销申请'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '指数型'

    @allure.severity("critical")
    @allure.story("测试交易记录")
    @allure.title("基金修改分红方式申请交易记录")
    def test_modify_dividened_record(self):
        self.trade_record.setup(BasePage(self).get_data()['test_trade_record']['_device_name'])
        self.trade_record.swap_guide_and_go_to_different_pages(4)
        self.trade_record.login_and_go_to_other_pages(BasePage(self).get_data()['test_trade_record']['_mobile_1'],
                                                      BasePage(self).get_data()['test_trade_record']['_pwd_1'], tag=9)
        self.trade_record.trade_apply_select_trade_type(trade_type='修改分红方式')
        time.sleep(5)
        if TradeApplyRecords.get_record_state(self.trade_record.ll) == '确认中':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_status(self.trade_record.ll) == '确认中'
        elif TradeApplyRecords.get_record_state(self.trade_record.ll) == '撤单':
            TradeApplyRecords.click_trade_record(self.trade_record.ll)
            assert TradeRecordDetails.get_status(self.trade_record.ll) == '撤单'
        assert TradeRecordDetails.get_trade_type(self.trade_record.ll) == '设置分红方式'
        assert TradeRecordDetails.get_fund_type(self.trade_record.ll) == '指数型'
