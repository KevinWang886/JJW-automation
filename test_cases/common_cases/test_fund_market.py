import time
import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.fund_market_page import FundMarketPage
from page.fund_order_page import FundOrderPage


class TestFundMarket:

    fund_market = PublicMethod()

    @allure.severity("normal")
    @allure.story("测试基金超市")
    @allure.title("基金排行")
    def test_fund_order(self):
        self.fund_market.setup(BasePage(self).get_data()['test_fund_market']['_device_name'])
        self.fund_market.swap_guide_and_go_to_different_pages(3)
        FundMarketPage.click_fund_rank(self.fund_market.ll)
        FundOrderPage.click_filter_btn(self.fund_market.ll)
        FundOrderPage.select_daily(self.fund_market.ll)
        FundOrderPage.select_can_buy(self.fund_market.ll)
        time.sleep(1)
        BasePage.click_physical_keys(self.fund_market.ll, 4)  # 点击物理键返回
        assert FundOrderPage.get_order_text(self.fund_market.ll) == \
               BasePage(self).get_data()['test_fund_market']['_order_text']
        FundOrderPage.click_zhaiquan_tab(self.fund_market.ll)
        assert FundOrderPage.get_order_text(self.fund_market.ll) == \
               BasePage(self).get_data()['test_fund_market']['_order_text']
        FundOrderPage.click_hunhe_tab(self.fund_market.ll)
        assert FundOrderPage.get_order_text(self.fund_market.ll) == \
               BasePage(self).get_data()['test_fund_market']['_order_text']
        FundOrderPage.click_huobi_tab(self.fund_market.ll)
        assert FundOrderPage.get_order_text(self.fund_market.ll) == \
               BasePage(self).get_data()['test_fund_market']['_order_text_2']

    @allure.severity("normal")
    @allure.story("测试基金超市")
    @allure.title("明星基金")
    def test_star_fund(self):
        self.fund_market.setup(BasePage(self).get_data()['test_fund_market']['_device_name'])
        self.fund_market.swap_guide_and_go_to_different_pages(3)
        FundMarketPage.click_star_fund(self.fund_market.ll)
        assert self.fund_market.get_page_title() == BasePage(self).get_data()['test_fund_market']['_star_fund_title']

    @allure.severity("normal")
    @allure.story("测试基金超市")
    @allure.title("信息披露")
    def test_info_disclosure(self):
        self.fund_market.setup(BasePage(self).get_data()['test_fund_market']['_device_name'])
        self.fund_market.swap_guide_and_go_to_different_pages(3)
        FundMarketPage.click_info_disclosure(self.fund_market.ll)
        assert self.fund_market.get_page_title() == \
               BasePage(self).get_data()['test_fund_market']['_info_disclosure_title']

    @allure.severity("normal")
    @allure.story("测试基金超市")
    @allure.title("新手学堂")
    def test_new_school(self):
        self.fund_market.setup(BasePage(self).get_data()['test_fund_market']['_device_name'])
        self.fund_market.swap_guide_and_go_to_different_pages(3)
        FundMarketPage.click_new_school(self.fund_market.ll)
        assert self.fund_market.get_page_title() == BasePage(self).get_data()['test_fund_market']['_new_school_title']

    @allure.severity("normal")
    @allure.story("测试基金超市")
    @allure.title("基金推荐/热门/主题tab")
    def test_advise_tab(self):
        self.fund_market.setup(BasePage(self).get_data()['test_fund_market']['_device_name'])
        self.fund_market.swap_guide_and_go_to_different_pages(3)
        assert FundMarketPage.get_tab_fund_list(self.fund_market.ll) == 5
        FundMarketPage.click_hot_tab(self.fund_market.ll)
        assert FundMarketPage.get_tab_fund_list(self.fund_market.ll) == 5
        FundMarketPage.click_item_tab(self.fund_market.ll)
        assert FundMarketPage.get_tab_fund_list(self.fund_market.ll) == 5
