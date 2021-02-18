import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class FundFixBuy(BasePage):

    @allure.step('基金定投，新增定投计划')
    def add_fix_plan(self):
        # if self.is_element_exist(element=self.get_file_from_yaml()['fund_fix_buy']['_fund_list']) == True:
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_fix_buy']['_add_fix_plan'])
        # elif self.is_element_exist(element= 'com.linlong.fund.debug2:id/invest_btn') == True:
        #     CommonBlankPage.click_fix_buy()
        # else:
        #     self.log.info('未进入定投页面')

    @allure.step('基金定投，点击修改')
    def modify_plan(self):
        fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_fix_buy']['_modify'])
        if len(fund_list) > 0:
            fund_list[0].click()
        else:
            self.log.info("无定投计划")

    @allure.step('基金定投，暂停定投计划')
    def spause_plan(self):
        running_fix_plan = self.find_elements(By.XPATH, self.get_file_from_yaml()['fund_fix_buy']['_spause'])
        if len(running_fix_plan) > 0:
            running_fix_plan[0].click()
        else:
            self.log.info("无可暂停定投计划")

    @allure.step('基金定投，恢复定投计划')
    def renew_plan(self):
        spause_fix_plan = self.find_elements(By.XPATH, self.get_file_from_yaml()['fund_fix_buy']['_renew'])
        if len(spause_fix_plan) > 0:
            spause_fix_plan[0].click()
        elif len(spause_fix_plan) == 0:
            self.slip_up()
            spause_fix_plan = self.find_elements(By.XPATH, self.get_file_from_yaml()['fund_fix_buy']['_renew'])
            if len(spause_fix_plan) > 0:
                spause_fix_plan[0].click()
        else:
                self.log.info("无暂定状态定投计划")

    @allure.step('基金定投，点击终止')
    def stop_plan(self):
        fund_list = self.find_elements(By.ID, self.get_file_from_yaml()['fund_fix_buy']['_stop'])
        if len(fund_list) > 0:
            fund_list[0].click()
        else:
            self.log.info("无定投计划")

    @allure.step('点击【确定】，暂停定投计划')
    def click_confirm_btn(self):
        self.find_element_and_click(By.ID, self.get_file_from_yaml()['fund_fix_buy']['_alert_confirm'])

