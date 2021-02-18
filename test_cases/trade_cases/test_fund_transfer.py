import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.my_holding import MyHolding
from page.transfer_success_page import TransferSuccessPage


class TestFundTransfer:

    fund_transfer = PublicMethod()
    # transfer_share = random.randint(10, 20)
    # trade_type = '036'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("基金转换")
    def test_fund_transfer(self):
        self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
        self.fund_transfer.agree_private_annce_skip_guide_page(1)
        self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
                                                       BasePage(self).get_data()['test_fund_transfer']['_pwd'], 0, 7)
        MyHolding.click_holding_fund(self.fund_transfer.ll)
        self.fund_transfer.fund_holding_details(0)
        # FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
        self.fund_transfer.select_transfer_fund(BasePage(self).get_data()['test_fund_transfer']['_password'])
        # assert float(ConfirmTransferPage.get_transfer_share(self.fund_transfer.ll)) == float(self.transfer_share)
        # InputPassword.input_password(self.fund_transfer.ll)
        assert TransferSuccessPage.get_success_text(self.fund_transfer.ll) == \
               BasePage(self).get_data()['test_fund_transfer']['_success_text']
        self.fund_transfer.teardown()

    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("基金转换，转出份额小于最低转换份额")
    # def test_fund_transfer_smaller_than_lowest(self):
    #     self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
    #     self.fund_transfer.swap_guide_and_go_to_different_pages(4)
    #     self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
    #                                                    BasePage(self).get_data()['test_fund_transfer']['_pwd'], tag=2)
    #     FundTradePage.transfer_fund(self.fund_transfer.ll)
    #     time.sleep(1)
    #     FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
    #     lowest_share = SelectTransferFund.get_watermark_text(self.fund_transfer.ll)
    #     share = float(lowest_share) - 1.0
    #     self.fund_transfer.select_transfer_fund(int(share))
    #     assert BasePage.get_toast(self.fund_transfer.ll) == ("最低转出份额为%s0份" % float(lowest_share))
    #     self.fund_transfer.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("基金转换，转出份额大于可用份额")
    # def test_fund_transfer_larger_than_available(self):
    #     self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
    #     self.fund_transfer.swap_guide_and_go_to_different_pages(4)
    #     self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
    #                                                    BasePage(self).get_data()['test_fund_transfer']['_pwd'], tag=2)
    #     FundTradePage.transfer_fund(self.fund_transfer.ll)
    #     time.sleep(1)
    #     FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
    #     available_share = SelectTransferFund.get_available_share(self.fund_transfer.ll)
    #     print(available_share)
    #     share = float(available_share) + 1.0
    #     self.fund_transfer.select_transfer_fund(int(share))
    #     assert BasePage.get_toast(self.fund_transfer.ll) == ("转出份额不能超过可用份额(%s份)" % float(available_share))
    #     self.fund_transfer.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("基金转换，全部转出")
    # def test_fund_transfer_all(self):
    #     self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
    #     self.fund_transfer.swap_guide_and_go_to_different_pages(4)
    #     self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
    #                                                    BasePage(self).get_data()['test_fund_transfer']['_pwd'], tag=2)
    #     FundTradePage.transfer_fund(self.fund_transfer.ll)
    #     time.sleep(1)
    #     FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
    #     self.fund_transfer.select_transfer_fund_all()
    #     self.fund_transfer.confirm_and_input_pwd(trade_type=self.trade_type)
    #     assert TransferSuccessPage.get_success_text(self.fund_transfer.ll) == \
    #            BasePage(self).get_data()['test_fund_transfer']['_success_text']
    #     self.fund_transfer.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("基金转换，未选择转入基金")
    # def test_not_select_transfer_fund(self):
    #     self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
    #     self.fund_transfer.swap_guide_and_go_to_different_pages(4)
    #     self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
    #                                                    BasePage(self).get_data()['test_fund_transfer']['_pwd'], tag=2)
    #     FundTradePage.transfer_fund(self.fund_transfer.ll)
    #     time.sleep(1)
    #     FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
    #     self.fund_transfer.not_select_transfer_fund(self.transfer_share)
    #     assert BasePage.get_toast(self.fund_transfer.ll) == \
    #            BasePage(self).get_data()['test_fund_transfer']['_toast_text']
    #     self.fund_transfer.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("基金转换，未输入转出份额")
    # def test_not_input_transfer_amount(self):
    #     self.fund_transfer.setup(BasePage(self).get_data()['test_fund_transfer']['_device_name'])
    #     self.fund_transfer.swap_guide_and_go_to_different_pages(4)
    #     self.fund_transfer.login_and_go_to_other_pages(BasePage(self).get_data()['test_fund_transfer']['_mobile'],
    #                                                    BasePage(self).get_data()['test_fund_transfer']['_pwd'], tag=2)
    #     FundTradePage.transfer_fund(self.fund_transfer.ll)
    #     time.sleep(1)
    #     FundTransferPage.click_transfer_btn(self.fund_transfer.ll)
    #     self.fund_transfer.not_input_transfer_amount()
    #     assert BasePage.get_toast(self.fund_transfer.ll) == \
    #            BasePage(self).get_data()['test_fund_transfer']['_toast_text_1']
    #     self.fund_transfer.teardown()
