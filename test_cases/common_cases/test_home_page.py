import allure
from base.base_page import BasePage
from page.public_methods import PublicMethod
from page.fund_info import FundInfo
from page.home_page import HomePage
from page.hot_fund_page import HotFundPage


class TestHomePage:

    home_page = PublicMethod()

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("优选基金按钮")
    def test_hot_fund(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_hot_fund_btn(self.home_page.ll)
        assert self.home_page.get_page_title() == BasePage(self).get_data()['test_home_page']['_hot_fund_page_title']
        assert HotFundPage.get_fund_name(self.home_page.ll) == \
               BasePage(self).get_data()['test_home_page']['_hot_fund_page_first_fund_name']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("新发基金按钮")
    def test_new_fund(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_new_fund_btn(self.home_page.ll)
        assert self.home_page.get_page_title() == BasePage(self).get_data()['test_home_page']['_new_fund_page_title']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("活期理财")
    def test_hqlc(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_hqlc(self.home_page.ll)
        assert self.home_page.get_page_title() == BasePage(self).get_data()['test_home_page']['_hqlc_page_title']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("工资定投")
    def test_gzdt(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_gzdt(self.home_page.ll)
        assert self.home_page.get_page_title() == BasePage(self).get_data()['test_home_page']['_gzdt_page_title']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("平台实力")
    def test_ptsl(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_ptsl(self.home_page.ll)
        assert self.home_page.get_page_title() == BasePage(self).get_data()['test_home_page']['_ptsl_page_title']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("50秒开户按钮")
    def test_quick_reg(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        assert HomePage.get_quick_reg_btn_text(self.home_page.ll) == \
               BasePage(self).get_data()['test_home_page']['_quick_reg']
        HomePage.click_mine_btn(self.home_page.ll)
        self.home_page.login_and_go_to_other_pages(BasePage(self).get_data()['test_home_page']['_mobile'],
                                                   BasePage(self).get_data()['test_home_page']['_pwd'], tag=6)
        assert HomePage.get_quick_reg_btn_text(self.home_page.ll) == \
               BasePage(self).get_data()['test_home_page']['_share']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("推荐基金")
    def test_advise_fund(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        assert HomePage.get_advise_fund_count(self.home_page.ll) == \
               BasePage(self).get_data()['test_home_page']['_advise_fund_count']
        HomePage.click_advise_fund(self.home_page.ll)
        assert FundInfo.get_fund_name(self.home_page.ll) == BasePage(self).get_data()['test_home_page']['_fund_name']
        assert FundInfo.get_fund_code(self.home_page.ll) == BasePage(self).get_data()['test_home_page']['_fund_code']

    @allure.severity("normal")
    @allure.story("测试首页")
    @allure.title("理财咨询，更多")
    def test_finance_more_btn(self):
        self.home_page.setup(BasePage(self).get_data()['test_home_page']['_device_name'])
        self.home_page.swap_guide_and_go_to_different_pages(2)
        HomePage.click_more_btn(self.home_page.ll)

