import time
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.fund_info import FundInfo
from page.home_page import HomePage


class TestFundStatus:

    fund_status = PublicMethod()

    @allure.severity("normal")
    @allure.story("测试基金状态")
    @allure.title("基金认购基金状态")
    def test_subscribe_fund_status(self):
        self.fund_status.setup(BasePage(self).get_data()['test_fund_status']['_device_name'])
        self.fund_status.swap_guide_and_go_to_different_pages(2)
        HomePage.click_search_btn(self.fund_status.ll)
        self.fund_status.search_and_click(BasePage(self).get_data()['test_fund_status']['_fund_code_1'])
        time.sleep(5)
        assert FundInfo.get_fix_btn_status(self.fund_status.ll) == 'false'
        assert FundInfo.get_buy_btn_status(self.fund_status.ll) == 'true'
        self.fund_status.teardown()

    @allure.severity("normal")
    @allure.story("测试基金状态")
    @allure.title("基金申购基金状态")
    def test_buy_fund_status(self):
        self.fund_status.setup(BasePage(self).get_data()['test_fund_status']['_device_name'])
        self.fund_status.swap_guide_and_go_to_different_pages(2)
        HomePage.click_search_btn(self.fund_status.ll)
        self.fund_status.search_and_click(BasePage(self).get_data()['test_fund_status']['_fund_code_2'])
        assert FundInfo.get_fix_btn_status(self.fund_status.ll) == 'true'
        assert FundInfo.get_buy_btn_status(self.fund_status.ll) == 'true'
        self.fund_status.teardown()
