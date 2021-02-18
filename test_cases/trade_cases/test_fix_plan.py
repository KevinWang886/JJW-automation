import random
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.fix_plan_success import FixPlanSuccess


class TestFixPlan:

    fix_plan = PublicMethod()
    fix_amount = random.randint(100, 110)
    trade_type = '039'

    @allure.severity("critical")
    @allure.story("测试基金交易")
    @allure.title("新增基金定投")
    def test_add_fix_plan(self):
        self.fix_plan.setup(BasePage(self).get_data()['test_fix_plan']['_device_name'])
        self.fix_plan.agree_private_annce_skip_guide_page(1)
        self.fix_plan.login_and_go_to_other_pages(BasePage(self).get_data()['test_fix_plan']['_mobile'],
                                                  BasePage(self).get_data()['test_fix_plan']['_pwd'],
                                                  0, 2)
        self.fix_plan.search_and_click(BasePage(self).get_data()['test_fix_plan']['_fund_code'])
        self.fix_plan.fund_info(action=1)
        self.fix_plan.input_fix_plan(fix_amount=self.fix_amount)
        assert FixPlanSuccess.get_success_text(self.fix_plan.ll) == \
               BasePage(self).get_data()['test_fix_plan']['_success_text']
        self.fix_plan.teardown()

    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("修改基金定投计划")
    # def test_modify_fix_plan(self):
    #     self.fix_plan.setup(BasePage(self).get_data()['test_fix_plan']['_device_name'])
    #     self.fix_plan.swap_guide_and_go_to_different_pages(4)
    #     self.fix_plan.login_and_go_to_other_pages(BasePage(self).get_data()['test_fix_plan']['_mobile'],
    #                                               BasePage(self).get_data()['test_fix_plan']['_pwd'], tag=3)
    #     time.sleep(1)
    #     FundFixBuy.modify_plan(self.fix_plan.ll)
    #     self.fix_plan.input_fix_plan(fix_amount=self.fix_amount)
    #     self.fix_plan.confirm_and_input_pwd(trade_type=self.trade_type)
    #     assert FixPlanSuccess.get_success_text(self.fix_plan.ll) == \
    #            BasePage(self).get_data()['test_fix_plan']['_success_text']
    #     self.fix_plan.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("暂停基金定投计划")
    # def test_spause_fix_plan(self):
    #     self.fix_plan.setup(BasePage(self).get_data()['test_fix_plan']['_device_name'])
    #     self.fix_plan.swap_guide_and_go_to_different_pages(4)
    #     self.fix_plan.login_and_go_to_other_pages(BasePage(self).get_data()['test_fix_plan']['_mobile'],
    #                                               BasePage(self).get_data()['test_fix_plan']['_pwd'], tag=3)
    #     time.sleep(1)
    #     self.fix_plan.spause_or_stop_fix_plan(tag=1, trade_type='040')
    #     assert BasePage.get_toast(self.fix_plan.ll) == BasePage(self).get_data()['test_fix_plan']['_toast_text']
    #     self.fix_plan.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("恢复基金定投计划")
    # def test_renew_fix_plan(self):
    #     self.fix_plan.setup(BasePage(self).get_data()['test_fix_plan']['_device_name'])
    #     self.fix_plan.swap_guide_and_go_to_different_pages(4)
    #     self.fix_plan.login_and_go_to_other_pages(BasePage(self).get_data()['test_fix_plan']['_mobile'],
    #                                               BasePage(self).get_data()['test_fix_plan']['_pwd'], tag=3)
    #     time.sleep(1)
    #     self.fix_plan.spause_or_stop_fix_plan(tag=2, trade_type='040')
    #     assert BasePage.get_toast(self.fix_plan.ll) == BasePage(self).get_data()['test_fix_plan']['_toast_text']
    #     self.fix_plan.teardown()
    #
    # @allure.severity("normal")
    # @allure.story("测试基金交易")
    # @allure.title("终止基金定投计划")
    # def test_stop_fix_plan(self):
    #     self.fix_plan.setup(BasePage(self).get_data()['test_fix_plan']['_device_name'])
    #     self.fix_plan.swap_guide_and_go_to_different_pages(4)
    #     self.fix_plan.login_and_go_to_other_pages(BasePage(self).get_data()['test_fix_plan']['_mobile'],
    #                                               BasePage(self).get_data()['test_fix_plan']['_pwd'], tag=3)
    #     time.sleep(1)
    #     self.fix_plan.spause_or_stop_fix_plan(tag=3, trade_type='040')
    #     assert BasePage.get_toast(self.fix_plan.ll) == BasePage(self).get_data()['test_fix_plan']['_toast_text']
    #     self.fix_plan.teardown()
