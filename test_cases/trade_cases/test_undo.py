import random
import time
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.buy_fund_success import BuyFundSuccess
from page.fund_info import FundInfo
from page.fund_trade_page import FundTradePage
from page.fund_transfer_pay import FundTransferPage
from page.home_page import HomePage
from page.mine_page import MinePage
from page.redeem_page import RedeemPage
from page.redeem_success import RedeemSuccess
from page.transfer_success_page import TransferSuccessPage
from page.undo_success import UndoSuccess


class TestUndo:

    undo = PublicMethod()
    amount = random.randint(1, 99)
    share = random.randint(10, 20)
    trade_type = '022'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("申购撤单")
    def test_buy_undo(self):
        self.undo.setup(BasePage(self).get_data()['test_undo']['_device_name'])
        self.undo.swap_guide_and_go_to_different_pages(4)
        self.undo.login_and_go_to_other_pages(BasePage(self).get_data()['test_undo']['_mobile'],
                                              BasePage(self).get_data()['test_undo']['_pwd'], tag=6)
        HomePage.click_search_btn(self.undo.ll)
        self.undo.search_and_click(BasePage(self).get_data()['test_undo']['_fund_code'])
        FundInfo.click_buy_now(self.undo.ll)
        self.undo.input_buy_info(self.amount)
        self.undo.confirm_and_input_pwd(trade_type='022')
        assert BasePage(self).get_data()['test_undo']['_buy_success'] == BuyFundSuccess.get_success_text(self.undo.ll)
        BuyFundSuccess.click_done_btn(self.undo.ll)   # 购买成功页面点击完成
        FundInfo.click_return(self.undo.ll)   # 基金详情页点击返回按钮
        HomePage.click_mine_btn(self.undo.ll)  # 首页点击我的按钮进入我的页面
        MinePage.click_fund_trade(self.undo.ll)   # 我的页面点击基金交易
        FundTradePage.trade_undo(self.undo.ll)  # 基金交易页面点击交易撤单
        self.undo.trade_undo()
        assert UndoSuccess.get_success_text(self.undo.ll) == BasePage(self).get_data()['test_undo']['_success_text']
        assert UndoSuccess.get_trade_content(self.undo.ll) == BasePage(self).get_data()['test_undo']['_trade_content']
        self.undo.teardown()

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("赎回撤单")
    def test_redeem_undo(self):
        self.undo.setup(BasePage(self).get_data()['test_undo']['_device_name'])
        self.undo.swap_guide_and_go_to_different_pages(4)
        self.undo.login_and_go_to_other_pages(BasePage(self).get_data()['test_undo']['_mobile'],
                                              BasePage(self).get_data()['test_undo']['_pwd'], tag=2)
        FundTradePage.redeem_fund(self.undo.ll)
        self.undo.fund_redeem(0, self.share, "是")
        self.undo.confirm_and_input_pwd(trade_type='024')
        assert BasePage(self).get_data()['test_undo']['_success_text'] == RedeemSuccess.get_success_text(self.undo.ll)
        RedeemSuccess.click_done_btn(self.undo.ll)
        RedeemPage.click_return_btn(self.undo.ll)
        FundTradePage.trade_undo(self.undo.ll)
        self.undo.trade_undo()
        assert UndoSuccess.get_success_text(self.undo.ll) == BasePage(self).get_data()['test_undo']['_success_text']
        assert UndoSuccess.get_trade_content(self.undo.ll) == BasePage(self).get_data()['test_undo']['_trade_content']
        self.undo.teardown()

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("转换撤单")
    def test_transfer_undo(self):
        self.undo.setup(BasePage(self).get_data()['test_undo']['_device_name'])
        self.undo.swap_guide_and_go_to_different_pages(4)
        self.undo.login_and_go_to_other_pages(BasePage(self).get_data()['test_undo']['_mobile'],
                                              BasePage(self).get_data()['test_undo']['_pwd'], tag=2)
        FundTradePage.transfer_fund(self.undo.ll)
        time.sleep(1)
        FundTransferPage.click_transfer_btn(self.undo.ll)
        self.undo.select_transfer_fund(share=self.share)
        self.undo.confirm_and_input_pwd(trade_type='036')
        assert TransferSuccessPage.get_success_text(self.undo.ll) == \
               BasePage(self).get_data()['test_undo']['_success_text']
        TransferSuccessPage.click_done_btn(self.undo.ll)
        self.undo.click_return_btn()
        self.undo.trade_undo()
        assert UndoSuccess.get_success_text(self.undo.ll) == BasePage(self).get_data()['test_undo']['_success_text']
        assert UndoSuccess.get_trade_content(self.undo.ll) == BasePage(self).get_data()['test_undo']['_trade_content']
        self.undo.teardown()

