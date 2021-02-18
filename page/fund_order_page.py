import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundOrderPage(BasePage):

    @allure.step("选择基金")
    def select_fund(self):
        if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_fund_list']) == True:
            fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_order_page']['_fund_list'])
            fund_list[0].click()
        else:
            FundOrderPage.click_zhaiquan_tab(self)
            if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_fund_list']) == True:
                fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_order_page']['_fund_list'])
                fund_list[0].click()
            else:
                FundOrderPage.click_hunhe_tab(self)
                if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_fund_list']) == True:
                    fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_order_page']['_fund_list'])
                    fund_list[0].click()
                else:
                    FundOrderPage.click_zhishu_tab(self)
                    if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_fund_list']) == True:
                        fund_list = self.find_elements(By.ID,
                                                       self.get_file_from_yaml()['fund_order_page']['_fund_list'])
                        fund_list[0].click()

    @allure.step("点击搜索")
    def click_search_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_search_btn'])

    @allure.step("搜索基金")
    def search_fund(self, fund_code):
        self.send_keys(By.ID, self.get_file_from_yaml()['fund_order_page']['_search_box'], fund_code)

    @allure.step("点击搜索结果")
    def click_search_result(self):
        if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_search_fund']) == True:
            search_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_order_page']['_search_fund'])
            search_list[0].click()
        else:
            self.log.info("无搜索结果")

    @allure.step("点击债券tab")
    def click_zhaiquan_tab(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_order_page']['_zhaiquan'])

    @allure.step("点击混合tab")
    def click_hunhe_tab(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_order_page']['_hunhe'])

    @allure.step("点击指数tab")
    def click_zhishu_tab(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_order_page']['_zhishu'])

    @allure.step("点击货币tab")
    def click_huobi_tab(self):
        self.find_element_and_click(By.XPATH, self.get_file_from_yaml()['fund_order_page']['_huobi'])

    @allure.step("点击筛选按钮")
    def click_filter_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_filter_btn'])

    @allure.step("收益区间，选择日涨跌幅")
    def select_daily(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_daily'])

    @allure.step("收益区间，选择近一月")
    def select_one_month(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_one_month'])

    @allure.step("收益区间，选择近三月")
    def select_three_month(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_three_month'])

    @allure.step("收益区间，选择近六月")
    def select_six_month(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_six_month'])

    @allure.step("收益区间，选择近一年")
    def select_one_year(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_one_year'])

    @allure.step("投资类型，选择全部")
    def select_all_type(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_all_type'])

    @allure.step("投资类型，可购买")
    def select_can_buy(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_can_buy'])

    @allure.step("投资类型，可定投")
    def select_can_fix(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_order_page']['_can_fix'])

    @allure.step("获取排序规则文案")
    def get_order_text(self):
        if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_order_text']) == True:
            order_text = self.find_element(By.ID, self.get_file_from_yaml()['fund_order_page']['_order_text']).text
            return order_text
        else:
            FundOrderPage.click_zhaiquan_tab(self)
            if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_order_text']) == True:
                order_text = self.find_element(By.ID, self.get_file_from_yaml()['fund_order_page']['_order_text']).text
                return order_text
            else:
                FundOrderPage.click_hunhe_tab(self)
                if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_order_text']) == True:
                    order_text = self.find_element(By.ID,
                                                   self.get_file_from_yaml()['fund_order_page']['_order_text']).text
                    return order_text
                else:
                    FundOrderPage.click_zhishu_tab(self)
                    if self.is_element_exist(self.get_file_from_yaml()['fund_order_page']['_order_text']) == True:
                        order_text = self.find_element(By.ID,
                                                       self.get_file_from_yaml()['fund_order_page']['_order_text']).text
                        return order_text
                    else:
                        self.log.info("无基金")

