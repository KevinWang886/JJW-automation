from base.base_page import BasePage
from base.start_app import StartAPP
from page.Input_buy_fund_info import InputBuyFundInfo
from page.account_management_page import AccountManagementPage
from page.add_card_page import AddCardPage
from page.bind_card import BindCard
from page.bind_card_page import BindCardPage
from page.confirm_buy_info import ConfirmBuyInfo
from page.confirm_fix_plan import ConfirmFixPlan
from page.confirm_redeem import ConfirmRedeem
from page.confirm_transfer_page import ConfirmTransferPage
from page.confirm_undo import ConfirmUndo
from page.crs_details import CRSDetails
from page.crs_page import CRSPage
from page.fund_fix_buy import FundFixBuy
from page.fund_holding_details import FundHoldingDetails
from page.fund_info import FundInfo
from page.fund_order_page import FundOrderPage
from page.fund_trade_page import FundTradePage
from page.fund_transfer_pay import FundTransferPage
from page.guide_page import GuidePage
from page.input_fix_plan import InputFixPlan
from page.input_redeem_info import InputRedeemInfo
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.modify_dividend_page import ModifyDividendPage
from page.modify_email import ModifyEmail
from page.modify_mobile import ModifyMobile
from page.password import InputPassword
from page.person_info_page import PersonInfo
from page.product_page import ProductPage
from page.register_page import RegisterPage
from page.reset_pwd_page import ResetPwdPage
from page.reset_trade_pwd_page import ResetTradePwdPage
from page.search_page import SearchPage
from page.select_transfer_fund import SelectTransferFund
from page.set_dividend_page import SetDividendPage
from selenium.webdriver.common.by import By
from page.set_trade_pwd import SetTradePwd
from page.trade_query_page import TradeQueryPage
from page.trade_undo import TradeUndo
from page.trade_records_page import TradeRecordsPage


class PublicMethod:

    def setup(self, device_name):  # 启动APP
        self.ll = StartAPP().run_app(device_name)

    def teardown(self):  # 退出APP
        self.ll.driver.quit()

    def swap(self):  # 引导页，滑动屏幕
        GuidePage.slip_move_2(self.ll, ti=100)
        GuidePage.slip_move_2(self.ll, ti=100)

    def agree_private_annce_skip_guide_page(self, tag):
        GuidePage.click_agree_btn(self.ll)
        GuidePage.click_skip_btn(self.ll)
        ProductPage.close_ad(self.ll)
        ProductPage.go_to_different_page(self.ll, tag)




    # def swap_guide_and_go_to_different_pages(self, tag):    # 滑过引导页，进入不同页面
    #     PublicMethod.agree_private_annce(self)
    #     if tag == 0:  # 划过引导页，点击【马上体验】,弹出隐私协议
    #         GuidePage.click_go_btn(self.ll)
    #     elif tag == 1:   # 引导页进入注册页面
    #         GuidePage.click_go_register_btn(self.ll)
    #         PrivateInfo.click_agree(self.ll)
    #     elif tag == 2:   # 进入首页
    #         GuidePage.click_go_btn(self.ll)
    #         PrivateInfo.click_agree(self.ll)
    #     elif tag == 3:   # 进入基金超市页面
    #         GuidePage.click_go_btn(self.ll)
    #         PrivateInfo.click_agree(self.ll)
    #         HomePage.click_fund_market(self.ll)
    #     elif tag == 4:  # 进入登录页面
    #         GuidePage.click_go_btn(self.ll)
    #         PrivateInfo.click_agree(self.ll)
    #         HomePage.click_mine_btn(self.ll)

    def login(self, username, password):   # 输入账号密码，登录
        LoginPage.input_username(self.ll, username=username)
        LoginPage.input_password(self.ll, password=password)
        LoginPage.login_btn(self.ll)

    def login_without_password(self, mobile):   # 不输入密码，登录
        LoginPage.input_username(self.ll, mobile=mobile)

    def login_without_account(self, pwd):   # 不输入账号，登录
        LoginPage.input_password(self.ll, pwd=pwd)

    def login_and_gesture(self, username, password, gesture_flag):  # 0取消，1 开通
        PublicMethod.login(self, username, password)
        if gesture_flag == 0:
            LoginPage.cancel_gesture(self.ll)
        elif gesture_flag == 1:
            LoginPage.confirm_gesture(self.ll)

    def login_and_go_to_other_pages(self, username, password, gesture_flag, tag):    # 登录app并进入到其他页面
        PublicMethod.login_and_gesture(self, username, password, gesture_flag)
        if tag == 1:
            MinePage.go_to_account_management(self.ll)   # 进入账户管理页
        elif tag == 2:
            MinePage.go_to_product_page(self.ll)  # 进入产品页
        elif tag == 3:
            MinePage.go_to_driver_menu(self.ll)   # 进入驾驶室
        elif tag == 4:
            MinePage.go_to_famous_page(self.ll)   # 进入名人堂
        elif tag == 5:
            MinePage.click_create_group(self.ll)   # 点击创建组合
        elif tag == 6:
            MinePage.click_trade_record(self.ll)   # 点击交易记录
        elif tag == 7:
            MinePage.click_my_asserts(self.ll)   # 点击进入我的资产
        elif tag == 8:
            MinePage.click_fix_buy(self.ll)   # 点击基金定投
        elif tag == 9:
            MinePage.click_devidened_details(self.ll)   # 点击分红明细
        elif tag == 10:
            MinePage.click_my_focus(self.ll)   # 点击我的打赏/关注
        elif tag == 11:
            MinePage.click_share(self.ll)   # 进入邀请好友
        elif tag == 12:
            MinePage.click_my_selected(self.ll)  # 点击我的自选
        elif tag == 13:
            MinePage.click_my_mall(self.ll)  # 点击我的金基币
        elif tag == 14:
            MinePage.click_activity(self.ll)  # 点击我的金基币

    # def guide_and_login(self, tag, mobile, pwd):   # 划过引导页，进入登录页，并进行登录
    #     PublicMethod.agree_private_annce_skip_guide_page(self)
    #     PublicMethod.login(self, mobile, pwd)

    def fund_holding_details(self, trade_type):
        if trade_type == 0:
            FundHoldingDetails.click_transfer(self.ll)
        elif trade_type == 1:
            FundHoldingDetails.click_redeem(self.ll)
        elif trade_type == 2:
            FundHoldingDetails.click_add_buy(self.ll)
        elif trade_type == 3:
            FundHoldingDetails.click_fix_buy(self.ll)
        elif trade_type == 4:
            FundHoldingDetails.click_modify_profit(self.ll)
        elif trade_type == 5:
            FundHoldingDetails.click_everyday_income(self.ll)
        elif trade_type ==6:
            FundHoldingDetails.click_trade_records(self.ll)
        elif trade_type == 7:
            FundHoldingDetails.click_profit_records(self.ll)

    def logout(self, tag):  # 安全退出
        AccountManagementPage.click_logout(self.ll)
        if tag == 1:
            AccountManagementPage.confirm_logout(self.ll)
        elif tag == 0:
            AccountManagementPage.cancel_logout(self.ll)

    def modify_personal_info(self):
        PersonInfo.slip_up_or_down(self.ll, flag=2)
        PersonInfo.slip_up_or_down(self.ll, flag=3)
        PersonInfo.slip_up_or_down(self.ll, flag=4)
        PersonInfo.slip_up_or_down(self.ll, flag=1)
        PersonInfo.click_submit_btn(self.ll)
        InputPassword.input_password(self.ll)

    def trade_records(self, action, tag):
        if action == '交易类型':
            TradeRecordsPage.click_trade_type(self.ll)
            if tag == 0:
                TradeRecordsPage.select_buy(self.ll)
                assert TradeRecordsPage.get_record_type(self.ll) == "申购"
            elif tag == 1:
                TradeRecordsPage.select_redeem(self.ll)
                assert TradeRecordsPage.get_record_type(self.ll) == "赎回"
            elif tag == 2:
                TradeRecordsPage.select_transfer(self.ll)
                assert TradeRecordsPage.get_record_type(self.ll) == "转换"
            elif tag == 3:
                TradeRecordsPage.select_fix(self.ll)
                assert TradeRecordsPage.get_record_type(self.ll) == "定投"
        elif action == '交易状态':
            TradeRecordsPage.click_trade_status(self.ll)
            if tag == 0:
                TradeRecordsPage.select_confirming(self.ll)
                assert TradeRecordsPage.get_record_state(self.ll) == "确认中"
            elif tag == 1:
                TradeRecordsPage.select_confirm_success(self.ll)
                assert TradeRecordsPage.get_record_state(self.ll) == "确认成功"
            elif tag == 4:
                TradeRecordsPage.select_confirm_fail(self.ll)
                assert TradeRecordsPage.get_record_state(self.ll) == "确认失败"
            elif tag == 3:
                TradeRecordsPage.select_trade_fail(self.ll)
                assert TradeRecordsPage.get_record_state(self.ll) == "交易失败"
            elif tag == 2:
                TradeRecordsPage.select_undo(self.ll)
                assert TradeRecordsPage.get_record_state(self.ll) == "已撤单"

    # def modify_id_valid_date(self):   # 修改身份证有效期
    #     PersonInfo.id_valid_date(self.ll)
    #     PersonInfo.select_id_valid_date(self.ll)
    #     PersonInfo.click_confirm_btn(self.ll)
    #
    # def modify_id_valid_date_long_time(self):    # 修改身份证有效期为长期有效
    #     PersonInfo.id_valid_date(self.ll)
    #     PersonInfo.select_id_valid_date_long_time(self.ll)
    #
    # def modify_professor(self):   # 修改职业
    #     if PersonInfo.get_current_professor(self.ll) == '其他':
    #         PersonInfo.click_professor(self.ll)
    #         PersonInfo.select_professor_down(self.ll)
    #     else:
    #         PersonInfo.click_professor(self.ll)
    #         PersonInfo.select_professor_up(self.ll)
    #     PersonInfo.click_confirm_btn(self.ll)
    #
    # def modify_marriage_status(self):  # 修改婚姻状态
    #     if BasePage.is_element_exist(self.ll,
    #                                  BasePage.get_file_from_yaml(self.ll)['person_info']['_current_marriage']) == True:
    #         if PersonInfo.get_current_marriage(self.ll) == '已婚':
    #             PersonInfo.click_marriage_status(self.ll)
    #             PersonInfo.select_marriage_down(self.ll)
    #         else:
    #             PersonInfo.click_marriage_status(self.ll)
    #             PersonInfo.select_marriage_up(self.ll)
    #     else:
    #         PersonInfo.click_marriage_status(self.ll)
    #         PersonInfo.select_marriage_down(self.ll)
    #     PersonInfo.click_confirm_btn(self.ll)
    #
    # def modify_education(self):  # 修改学历
    #     if BasePage.is_element_exist(self.ll,
    #                                  BasePage.get_file_from_yaml(self.ll)['person_info']['_current_education']) == True:
    #         if PersonInfo.get_current_education(self.ll) == '硕士及以上':
    #             PersonInfo.click_education(self.ll)
    #             PersonInfo.select_education_down(self.ll)
    #         else:
    #             PersonInfo.click_education(self.ll)
    #             PersonInfo.select_education_up(self.ll)
    #     else:
    #         PersonInfo.click_education(self.ll)
    #         PersonInfo.select_education_down(self.ll)
    #     PersonInfo.click_confirm_btn(self.ll)
    #
    # def modify_annual_income(self):  # 修改年收入
    #     if BasePage.is_element_exist(self.ll,
    #                                  BasePage.get_file_from_yaml(self.ll)['person_info']['_current_annual_income']) == True:
    #         if PersonInfo.get_current_annual_income(self.ll) == '500W以上':
    #             PersonInfo.click_annual_income(self.ll)
    #             PersonInfo.select_annual_income_down(self.ll)
    #         else:
    #             PersonInfo.click_annual_income(self.ll)
    #             PersonInfo.select_annual_income_up(self.ll)
    #     else:
    #         PersonInfo.click_annual_income(self.ll)
    #         PersonInfo.select_annual_income_down(self.ll)
    #     PersonInfo.click_confirm_btn(self.ll)
    #
    # def modify_person_info(self):   # 修改个人信息
    #     PublicMethod.modify_id_valid_date(self)
    #     PublicMethod.modify_professor(self)
    #     PublicMethod.modify_marriage_status(self)
    #     PublicMethod.modify_education(self)
    #     PublicMethod.modify_annual_income(self)
    #     PersonInfo.click_submit_btn(self.ll)
    #     InputPassword.input_password(self.ll)

    def reset_trade_pwd(self, id_no, name, mobile, verify_code, pwd, confirm_pwd):  # 重置登录密码
        ResetTradePwdPage.input_id_no(self.ll, id_no=id_no)
        ResetTradePwdPage.input_name(self.ll, name=name)
        ResetTradePwdPage.input_mobile(self.ll, mobile=mobile)
        ResetTradePwdPage.input_verify_code(self.ll, verify_code=verify_code)
        # ResetTradePwdPage.get_code(self.ll)
        # if BasePage.get_toast(self.ll) == '已发送':
        #     ResetTradePwdPage.input_verify_code(self.ll, verify_code=verify_code)
        # else:
        #     print("请发送验证码")
        #     ResetTradePwdPage.get_code(self.ll)
        ResetTradePwdPage.input_pwd(self.ll, pwd=pwd)
        ResetTradePwdPage.input_confirm_pwd(self.ll, confirm_pwd=confirm_pwd)
        ResetTradePwdPage.click_confirm_btn(self.ll)

    def reset_pwd(self, mobile, verify_code, pwd, confirm_pwd):  # 重置登录密码
        ResetPwdPage.input_mobile(self.ll, mobile=mobile)
        ResetPwdPage.input_verify_code(self.ll, verify_code=verify_code)
        # ResetPwdPage.get_code(self.ll)
        # if BasePage.get_toast(self.ll) == '已发送':
        #     ResetPwdPage.input_verify_code(self.ll, verify_code=verify_code)
        # else:
        #     print("请发送验证码")
        #     ResetPwdPage.get_code(self.ll)
        ResetPwdPage.input_pwd(self.ll, pwd=pwd)
        ResetPwdPage.input_confirm_pwd(self.ll, confirm_pwd=confirm_pwd)
        ResetPwdPage.click_confirm_btn(self.ll)

    def search_and_click(self, fund_code):    # 输入搜索内容，并点击搜索结果
        ProductPage.click_search_btn(self.ll)
        SearchPage.input_info(self.ll, fund_code=fund_code)
        SearchPage.click_search_result(self.ll)

    def input_buy_info(self, amount, pwd):   # 输入购买信息
        lowest_amount = InputBuyFundInfo.get_lowest_amount(self.ll)
        if float(amount) < float(lowest_amount):
            InputBuyFundInfo.input_buy_amount(self.ll, amount)
            InputBuyFundInfo.check_announcement(self.ll)
            InputBuyFundInfo.click_next_btn(self.ll)
            assert BasePage.get_toast(self.ll) == '最低购买金额为%s元' % lowest_amount
        else:
            InputBuyFundInfo.input_buy_amount(self.ll, amount)
            InputBuyFundInfo.check_announcement(self.ll)
            InputBuyFundInfo.click_next_btn(self.ll)
            InputPassword.input_password(self.ll, pwd)
            # if BasePage.is_element_exist(self.ll,
            #                              BasePage.get_file_from_yaml(self.ll)
            #                              ['input_buy_fund_info']['_confirm_alert']) == True:
            #     # InputBuyFundInfo.confirm_alert(self.ll)
            # else:
            #     print("进入到确认定投计划页面")

    def opposite_actions_in_buy_fund(self, tag):
        if tag == 0:     # 未输入购买金额
            InputBuyFundInfo.check_announcement(self.ll)
        elif tag == 1:    # 未勾选协议
            InputBuyFundInfo.input_buy_amount(self.ll, 1000)
        elif tag == 2:    # 输入金额大于银行卡限额
            InputBuyFundInfo.input_buy_amount(self.ll, 1000000)
        elif tag == 3:    # 输入金额小于最低起投
            InputBuyFundInfo.input_buy_amount(self.ll, 1)
        assert InputBuyFundInfo.get_next_btn_status(self.ll) == 'false'

    def input_amount_larger_than_card_limit(self):    # 输入比银行卡单笔限额大的购买金额
        # card_limit = InputBuyFundInfo.get_bank_limit_amount(self.ll)
        # print(card_limit)
        # if float(card_limit) == float(9999):
        #     InputBuyFundInfo.input_buy_amount(self.ll, int(float(card_limit)+1.0))
        # elif float(card_limit) == float(1000):
        #     InputBuyFundInfo.input_buy_amount(self.ll, int(float(card_limit) + 1.0))
        # elif float(card_limit) == float(5):
        InputBuyFundInfo.input_buy_amount(self.ll, 1000000)

    def calculate_market_value(self):   # 计算基金当前市值
        calculate_market_value = FundTransferPage.get_hold_share * FundTransferPage.get_nav_value
        return round(calculate_market_value, 2)

    def select_transfer_fund(self, pwd):   # 输入转出份额，选择转换入基金，勾选协议，点击下一步按钮
        SelectTransferFund.click_transfer_twenty(self.ll)
        SelectTransferFund.click_transfer_fund(self.ll)
        SelectTransferFund.select_fund(self.ll)
        # SelectTransferFund.click_checkbox(self.ll)
        SelectTransferFund.click_next_btn(self.ll)
        if BasePage.is_element_exist(self.ll, BasePage.get_file_from_yaml(self.ll)['select_transfer_fund'][
                                         '_tip_content']) == True:
            SelectTransferFund.confirm_tip(self.ll)
            InputPassword.input_password(self.ll)
        else:
            InputPassword.input_password(self.ll, pwd)

    # def not_input_transfer_amount(self):   # 未输入转出份额，选择转换入基金，勾选协议，点击下一步按钮
    #     SelectTransferFund.click_transfer_fund(self.ll)
    #     SelectTransferFund.select_fund(self.ll)
    #     SelectTransferFund.click_checkbox(self.ll)
    #     SelectTransferFund.click_next_btn(self.ll)
    #
    # def not_select_transfer_fund(self, share):   # 输入转出份额，未选择转换入基金，勾选协议，点击下一步按钮
    #     SelectTransferFund.input_transfer_share(self.ll, share)
    #     SelectTransferFund.click_checkbox(self.ll)
    #     SelectTransferFund.click_next_btn(self.ll)
    #
    # def select_transfer_fund_all(self):   # 输入全部转出，选择转换入基金，勾选协议，点击下一步按钮
    #     SelectTransferFund.click_transfer_all(self.ll)
    #     SelectTransferFund.click_transfer_fund(self.ll)
    #     SelectTransferFund.select_fund(self.ll)
    #     SelectTransferFund.click_checkbox(self.ll)
    #     SelectTransferFund.click_next_btn(self.ll)

    def set_dividend(self, trade_type):  # 设置分红
        FundTradePage.set_dividend(self.ll)
        SetDividendPage.click_modify_dividend(self.ll)
        ModifyDividendPage.click_confirm_btn(self.ll)
        PublicMethod.confirm_and_input_pwd(self, trade_type)

    def fix_buy(self, fund_code):  # 基金定投
        FundFixBuy.add_fix_plan(self.ll)
        PublicMethod.search_fund_in_fund_order_page(self, fund_code)
        FundInfo.click_fix_buy(self.ll)

    def search_fund_in_fund_order_page(self, fund_code):    # 基金排行页面搜索基金并点击搜索结果
        FundOrderPage.click_search_btn(self.ll)
        FundOrderPage.search_fund(self.ll, fund_code)
        FundOrderPage.click_search_result(self.ll)

    def select_fix_cycle(self):    # 选择定投周期
        if BasePage.is_element_exist(self.ll,
                                     BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_fix_cycle_value']) == False:
            InputFixPlan.select_fix_cycle(self.ll)
            InputFixPlan.click_confirm_btn(self.ll)
        else:
            if InputFixPlan.get_fix_cycle(self.ll) == '每月':  # 如果当日定投周期已选择每月，进入定投周期，选择每周
                InputFixPlan.select_fix_cycle(self.ll)
                InputFixPlan.slip_control_btn_up(self.ll, By.ID,
                                                BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)
            else:
                InputFixPlan.select_fix_cycle(self.ll)
                InputFixPlan.slip_control_btn_down(self.ll, By.ID,
                                                BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)

    def select_fix_date(self):    # 选择定投日期
        if BasePage.is_element_exist(self.ll,
                                     BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_fix_date_value']) == False:
            InputFixPlan.select_fix_date(self.ll)
            InputFixPlan.click_confirm_btn(self.ll)
        else:
            if InputFixPlan.get_fix_date(self.ll) == '1':
                InputFixPlan.select_fix_date(self.ll)
                InputFixPlan.slip_control_btn_up(self.ll, By.ID,
                                                BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)
            elif InputFixPlan.get_fix_date(self.ll) == '周五':
                InputFixPlan.select_fix_date(self.ll)
                InputFixPlan.slip_control_btn_up(self.ll, By.ID,
                                                 BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)
            else:
                InputFixPlan.select_fix_date(self.ll)
                InputFixPlan.slip_control_btn_down(self.ll, By.ID,
                                                   BasePage.get_file_from_yaml(self.ll)['input_fix_plan'][
                                                       '_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)

    def select_pay_fail_type(self):   # 如果定投失败，选择扣款方式
        if BasePage.is_element_exist(self.ll,
                                     BasePage.get_file_from_yaml(self.ll)['input_fix_plan']['_pay_fail_value']) == False:
            InputFixPlan.select_pay_fail_type(self.ll)
            InputFixPlan.click_confirm_btn(self.ll)
        else:
            if InputFixPlan.get_pay_fail_value(self.ll) == '当期不再扣':  # 如果当日定投周期已选择每月，进入定投周期，选择每周
                InputFixPlan.select_pay_fail_type(self.ll)
                InputFixPlan.slip_control_btn_up(self.ll, By.ID,
                                                 BasePage.get_file_from_yaml(self.ll)['input_fix_plan'][
                                                     '_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)
            else:
                InputFixPlan.select_pay_fail_type(self.ll)
                InputFixPlan.slip_control_btn_down(self.ll, By.ID,
                                                   BasePage.get_file_from_yaml(self.ll)['input_fix_plan'][
                                                       '_picker_box'])
                InputFixPlan.click_confirm_btn(self.ll)

    def fund_info(self, action):
        if action == 0:
            FundInfo.click_buy_now(self.ll)
        elif action == 1:
            FundInfo.click_fix_buy(self.ll)
        elif action == 2:
            FundInfo.click_add_selection(self.ll)

    def input_fix_plan(self, fix_amount, pwd):   # 输入定投计划
        InputFixPlan.input_fix_amount(self.ll, fix_amount)
        PublicMethod.select_fix_cycle(self)
        PublicMethod.select_fix_date(self)
        # PublicMethod.select_pay_fail_type(self)
        InputFixPlan.click_checkbox(self.ll)
        InputFixPlan.click_next_btn(self.ll)
        InputPassword.input_password(self.ll, pwd)
        # InputFixPlan.confirm_alert(self.ll)

    def confirm_and_input_pwd(self, trade_type):   # 点击确定并输入交易密码
        if trade_type == '022':   # 申购
            ConfirmBuyInfo.click_confirm_buy_btn(self.ll)
        elif trade_type == '039':   # 新增定投
            ConfirmFixPlan.click_confirm_btn(self.ll)
        elif trade_type == '040':   # 终止、恢复、暂停定投计划
            ConfirmFixPlan.click_confirm(self.ll)
        elif trade_type == '036':   # 转换
            ConfirmTransferPage.click_confirm_btn(self.ll)
        elif trade_type == '024':  # 赎回
            ConfirmRedeem.click_confirm_redeem(self.ll)
        elif trade_type == '029':   # 修改分红方式
            ModifyDividendPage.click_confirm_btn(self.ll)
        elif trade_type == '020':   # 认购
            ConfirmBuyInfo.click_confirm_buy_btn(self.ll)
        InputPassword.input_password(self.ll)

    def spause_or_stop_fix_plan(self, tag, trade_type):   # 暂停定投计划
        if tag == 1:
            FundFixBuy.spause_plan(self.ll)   # 暂停定投计划
        elif tag == 2:
            FundFixBuy.renew_plan(self.ll)   # 恢复定投计划
        elif tag == 3:
            FundFixBuy.stop_plan(self.ll)   # 终止定投计划
        PublicMethod.confirm_and_input_pwd(self, trade_type)

    def add_bank_card(self, card_no, mobile_no, verify_code, trade_pwd):   # 添加银行卡，绑定银行卡
        AddCardPage.click_add_card(self.ll)
        BindCardPage.click_bank_card(self.ll)
        BindCardPage.select_card(self.ll)
        BindCardPage.input_card_no(self.ll, card_no)
        BindCardPage.input_mobile_no(self.ll, mobile_no)
        BindCardPage.get_verify_code(self.ll)
        BindCardPage.input_verify_code(self.ll, verify_code)
        BindCardPage.input_trade_pwd(self.ll, trade_pwd)
        BindCardPage.click_confirm_btn(self.ll)

    def register_account(self, tag, mobile, verify_code, pwd, confirm_pwd):    # 注册账号
        if tag == 0:  # 输入所有信息，注册账号
            RegisterPage.input_mobile(self.ll, mobile)
            RegisterPage.input_verify_code(self.ll, verify_code)
            RegisterPage.input_pwd(self.ll, pwd)
            RegisterPage.input_confirm_pwd(self.ll, confirm_pwd)
        elif tag == 1:   # 输入除手机号外所有信息，注册账号
            RegisterPage.input_verify_code(self.ll, verify_code)
            RegisterPage.input_pwd(self.ll, pwd)
            RegisterPage.input_confirm_pwd(self.ll, confirm_pwd)
        elif tag == 2:   # 输入除验证码外所有信息，注册账号
            RegisterPage.input_mobile(self.ll, mobile)
            RegisterPage.input_pwd(self.ll, pwd)
            RegisterPage.input_confirm_pwd(self.ll, confirm_pwd)
        elif tag == 3:   # 输入登录密码外所有信息，注册账号
            RegisterPage.input_mobile(self.ll, mobile)
            RegisterPage.input_verify_code(self.ll, verify_code)
            RegisterPage.input_confirm_pwd(self.ll, confirm_pwd)
        elif tag == 4:   # 输入确认登录密码外所有信息，注册账号
            RegisterPage.input_mobile(self.ll, mobile)
            RegisterPage.input_verify_code(self.ll, verify_code)
            RegisterPage.input_pwd(self.ll, pwd)
        RegisterPage.click_next_btn(self.ll)

    def bind_card(self, name, id_no, card_no, mobile, verify_code):   # 注册流程，绑定银行卡
        BindCard.input_name(self.ll, name)
        BindCard.input_id_card_no(self.ll, id_no)
        BindCard.click_valid_date(self.ll)
        BindCard.select_long_time(self.ll)
        BindCard.input_card_no(self.ll, card_no)
        BindCard.click_open_bank(self.ll)
        BindCard.select_bank(self.ll)
        BindCard.click_address(self.ll)
        BindCard.click_city(self.ll)
        BindCard.select_province(self.ll)
        BindCard.select_city(self.ll)
        BindCard.click_save(self.ll)
        BindCard.click_professor(self.ll)
        BindCard.click_confirm_btn(self.ll)
        BindCard.input_mobile_no(self.ll, mobile)
        BindCard.get_verify_code(self.ll)
        if BasePage.get_toast(self.ll) == "已发送":
            BindCard.input_verify_code(self.ll, verify_code)
        else:
            BindCard.get_verify_code(self.ll)
            BindCard.input_verify_code(self.ll, verify_code)
        BindCard.click_next_btn(self.ll)

    def set_trade_pwd(self, trade_pwd, confirm_trade_pwd):   # 重置交易密码
        SetTradePwd.input_trade_pwd(self.ll, trade_pwd)
        SetTradePwd.input_confirm_trade_pwd(self.ll, confirm_trade_pwd)
        SetTradePwd.click_next_btn(self.ll)

    def input_redeem_info(self, redeem_share, tag, pwd):    # 输入赎回信息，并点下一步
        lowest_redeem_share = InputRedeemInfo.get_watermark(self.ll)
        available_share = InputRedeemInfo.get_available_share(self.ll)
        if tag == 0:
            InputRedeemInfo.input_redeem_share(self.ll, redeem_share)
            if float(redeem_share) < float(lowest_redeem_share):    # 输入赎回份额小于最低赎回份额
                InputRedeemInfo.click_confirm_redeem_btn(self.ll)
            elif float(redeem_share) > float(available_share):   # 输入赎回份额大于持有份额
                InputRedeemInfo.click_confirm_redeem_btn(self.ll)
            else:    # 除以上情况外的情况
                # InputRedeemInfo.click_confirm_redeem_btn(self.ll)
                # if delay_status == '是':
                #     InputRedeemInfo.click_confirm_redeem_btn(self.ll)
                # elif delay_status == '否':
                InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        elif tag == 1:
            InputRedeemInfo.click_twenty_percent(self.ll)
            InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        elif tag == 2:
            InputRedeemInfo.click_thirty_percent(self.ll)
            InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        elif tag == 3:
            InputRedeemInfo.click_fifty_percent(self.ll)
            InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        elif tag == 4:
            InputRedeemInfo.click_redeem_all(self.ll)
            InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        InputPassword.input_password(self.ll, pwd)

    def redeem_all(self):   # 输入赎回信息页，点全部赎回，并点下一步
        InputRedeemInfo.click_redeem_all(self.ll)
        InputRedeemInfo.click_confirm_redeem_btn(self.ll)
        # if delay_status == '是':
        #     InputRedeemInfo.click_confirm_btn(self.ll)
        # elif delay_status == '否':
        #     InputRedeemInfo.click_cancel_btn(self.ll)

    def fund_redeem(self, tag, redeem_share):   # 基金赎回
        if tag == 0:   # tag为0时，部分赎回
            PublicMethod.input_redeem_info(self, redeem_share)
        elif tag == 1:   # tag为1时，全部赎回
            PublicMethod.redeem_all(self)
        elif tag == 2:    # 不输入赎回份额，直接点击下一步
            InputRedeemInfo.click_confirm_redeem_btn(self.ll)

    # def total_income(self):   # 我的持仓页面，将每支基金的当前收益相加求和算出总收益
    #     income = HoldDetails.get_current_income(self.ll)   # 获取当前收益数组
    #     sum = 0.00
    #     for i in income:
    #         sum = sum + float(i.text)    # 每支基金当前收益求和
    #     return sum

    # def total_market_value(self):  # 我的持仓页面，计算每支持仓基金的市值并相加算出总市值
    #     lastest_net = HoldDetails.get_latest_net(self.ll)   # 获取最新净值数组
    #     hold_share = HoldDetails.get_hold_share(self.ll)   # 获取基金的持有份额数组
    #     market_value = 0.00
    #     for i in lastest_net:   # 遍历出最新净值数组中的没一个最新净值
    #         for j in hold_share:   # 遍历出每支基金的持有份额
    #             market_value = market_value + float(i.text)*float(j.text)   # 最新净值*持有份额并且相加算出所有的市值
    #     return round(market_value, 2)   # 总市值保留2位小数

    def trade_undo(self):   # 交易撤单页面点击撤单，在撤单确认页面点击确认撤单,并输入交易密码完成撤单
        TradeUndo.click_undo_btn(self.ll)
        ConfirmUndo.click_confirm_undo_btn(self.ll)
        InputPassword.input_password(self.ll)

    def click_return_btn(self):  # 公共方法：点击返回按钮
        BasePage(self.ll).find_element_and_click(By.ID, 'left_btn')

    def get_page_title(self):  # 公共方法：获取页面标题
        page_title = BasePage(self.ll).find_element(By.ID, 'title_tv').text
        return page_title

    def modify_email(self, tag, new_email, login_pwd):    # 修改邮箱
        if tag == 0:   # 修改邮箱，输入邮箱，直接点击确认按钮
            ModifyEmail.input_new_email(self.ll, new_email)  # 输入新邮箱
            ModifyEmail.input_login_pwd(self.ll, login_pwd)   # 输入登录密码
        elif tag == 1:   # 修改邮箱，不输入新邮件，直接点击确认按钮
            ModifyEmail.input_login_pwd(self.ll, login_pwd)
        elif tag == 2:   # 修改邮箱，不输入登录密码，直接点击确认按钮
            ModifyEmail.input_new_email(self.ll, new_email)
        elif tag == 3:   # 不输入邮箱和登录密码
            BasePage(self).log.info("点击确认按钮")
        ModifyEmail.click_confirm_btn(self.ll)   # 点击确认按钮

    def modify_mobile(self, id_no, name, current_mobile, new_mobile, verify_code, trade_pwd):  # 输入信息修改手机号
        ModifyMobile.input_id_no(self.ll, id_no)   # 输入身份证号
        ModifyMobile.input_name(self.ll, name)  # 输入姓名
        ModifyMobile.input_current_mobile(self.ll, current_mobile)  # 输入当前手机号
        ModifyMobile.input_new_mobile(self.ll, new_mobile)  # 收入新手机号
        ModifyMobile.get_verify_code(self.ll)   # 获取短信验证码
        ModifyMobile.input_verify_code(self.ll, verify_code)   # 输入验证码
        ModifyMobile.input_trade_pwd(self.ll, trade_pwd)  # 输入交易密码
        ModifyMobile.click_confirm_btn(self.ll)   # 点击确认按钮

    def trade_apply_select_trade_type(self, trade_type):   # 进入交易申请查询，选择交易类型
        TradeQueryPage.click_apply_records(self.ll)
        TradeApplyRecords.click_trade_time(self.ll)
        TradeApplyRecords.select_all(self.ll)
        TradeApplyRecords.click_trade_type(self.ll)
        if trade_type == '认购':
            TradeApplyRecords.select_subscribe(self.ll)
        elif trade_type == '申购':
            TradeApplyRecords.select_buy(self.ll)
        elif trade_type == '赎回':
            TradeApplyRecords.select_redeem(self.ll)
        elif trade_type == '转换':
            TradeApplyRecords.select_transfer(self.ll)
        elif trade_type == '定投':
            TradeApplyRecords.select_fix(self.ll)
        elif trade_type == '撤单':
            TradeApplyRecords.select_undo(self.ll)
        elif trade_type == '修改分红方式':
            TradeApplyRecords.select_modify_dividend(self.ll)
        else:
            TradeApplyRecords.select_all(self.ll)

    def go_to_different_crs_page(self, tag):
        AccountManagementPage.click_crs(self.ll)
        if tag == 0:
            CRSPage.click_chinese_only(self.ll)
        elif tag == 1:
            CRSPage.click_not_china(self.ll)
        elif tag == 2:
            CRSPage.click_all(self.ll)
        CRSPage.click_confirm_btn(self.ll)

    def crs_details(self, lastname, firstname, live_address, birth_address, tax_number, tag):   # 选择非中国税收居民，填写税收居民信息
        CRSDetails.input_lastname(self.ll, lastname)
        CRSDetails.input_firstname(self.ll, firstname)
        CRSDetails.select_gender(self.ll)
        CRSDetails.select_birthday(self.ll)
        CRSDetails.select_live_country(self.ll)
        CRSDetails.input_live_address(self.ll, live_address)
        CRSDetails.select_birth_country(self.ll)
        CRSDetails.input_birth_address(self.ll, birth_address)
        CRSDetails.select_tax_country(self.ll)
        CRSDetails.input_tax_number(self.ll, tax_number)
        if tag == 1:
            BasePage.slip_up(self.ll)
            CRSDetails.click_submit_btn(self.ll)
        elif tag == 2:
            CRSDetails.click_add_tax_country(self.ll)
            BasePage.slip_up(self.ll)
            CRSDetails.select_tax_country(self.ll)
            CRSDetails.select_tax_reason(self.ll)
            CRSDetails.click_submit_btn(self.ll)


















