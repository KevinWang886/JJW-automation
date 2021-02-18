import random
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.input_redeem_info import InputRedeemInfo
from page.my_holding import MyHolding
from page.redeem_success import RedeemSuccess


class TestRedeem:

    redeem = PublicMethod()
    redeem_share = random.randint(10, 20)
    trade_type = '024'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("基金赎回")
    def test_redeem(self):
        self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
        self.redeem.agree_private_annce_skip_guide_page(1)
        self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
                                                  BasePage(self).get_data()['test_redeem']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.redeem.ll)
        self.redeem.fund_holding_details(1)
        self.redeem.input_redeem_info(self.redeem_share, tag=0)
        assert BasePage(self).get_data()['test_redeem']['_success_text'] == \
               RedeemSuccess.get_success_text(self.redeem.ll)

    # @allure.severity("critical")
    # @allure.story("测试基金交易")
    # @allure.title("基金赎回,不顺延赎回")
    # def test_redeem_not_delay(self):
    #     self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
    #     self.redeem.swap_guide_and_go_to_different_pages(1)
    #     self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
    #                                             BasePage(self).get_data()['test_redeem']['_pwd'], tag=2)
    #     FundTradePage.redeem_fund(self.redeem.ll)
    #     self.redeem.fund_redeem(0, self.redeem_share, "否")
    #     assert BasePage(self).get_data()['test_redeem']['_not_delay_redeem'] == \
    #            ConfirmRedeem.get_delay_redeem_status(self.redeem.ll)
    #     self.redeem.confirm_and_input_pwd(trade_type=self.trade_type)
    #     assert BasePage(self).get_data()['test_redeem']['_success_text'] == \
    #            RedeemSuccess.get_success_text(self.redeem.ll)
    #     assert float(self.redeem_share) == float(RedeemSuccess.get_redeem_share(self.redeem.ll))
    #
    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("全部赎回")
    def test_redeem_all(self):
        self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
        self.redeem.agree_private_annce_skip_guide_page(1)
        self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
                                                  BasePage(self).get_data()['test_redeem']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.redeem.ll)
        self.redeem.fund_holding_details(1)
        self.redeem.input_redeem_info(self.redeem_share, tag=4)
        assert BasePage(self).get_data()['test_redeem']['_success_text'] == RedeemSuccess.get_success_text(self.redeem.ll)

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("赎回份额小于最低赎回份额")
    def test_redeem_share_smaller_than_lowest(self):
        self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
        self.redeem.agree_private_annce_skip_guide_page(1)
        self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
                                                BasePage(self).get_data()['test_redeem']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.redeem.ll)
        self.redeem.fund_holding_details(1)
        self.redeem.input_redeem_info(redeem_share=0.1, tag=0)
        lowest_redeem_share = InputRedeemInfo.get_watermark(self.redeem.ll)
        assert BasePage.get_toast(self.redeem.ll) == ("最低赎回份额为%s0份" % float(lowest_redeem_share))

    @allure.severity("normal")
    @allure.story("测试基金交易")
    @allure.title("赎回份额大于可用份额")
    def test_redeem_share_larger_than_available_share(self):
        self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
        self.redeem.agree_private_annce_skip_guide_page(1)
        self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
                                                BasePage(self).get_data()['test_redeem']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.redeem.ll)
        self.redeem.fund_holding_details(1)
        self.redeem.input_redeem_info(redeem_share=100000000, tag=0)
        available_share = InputRedeemInfo.get_available_share(self.redeem.ll)
        assert BasePage.get_toast(self.redeem.ll) == ("赎回份额不能超过可用份额(%s份)" % float(available_share))
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("不输入赎回份额，直接点击下一步")
    # def test_not_input_redeem_share(self):
    #     self.redeem.setup(BasePage(self).get_data()['test_redeem']['_device_name'])
    #     self.redeem.swap_guide_and_go_to_different_pages(4)
    #     self.redeem.login_and_go_to_other_pages(BasePage(self).get_data()['test_redeem']['_mobile'],
    #                                             BasePage(self).get_data()['test_redeem']['_pwd'], tag=2)
    #     FundTradePage.redeem_fund(self.redeem.ll)
    #     RedeemPage.click_redeem_btn(self.redeem.ll)
    #     self.redeem.fund_redeem(2, self.redeem_share, "否")
    #     assert BasePage.get_toast(self.redeem.ll) == "请输入赎回份额"
