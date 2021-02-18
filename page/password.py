import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class InputPassword(BasePage):   # 交易密码
    @allure.step("输入交易密码")
    def input_password(self, pwd):    # 输入交易密码
        keyboard_size = self.find_element(By.ID, self.get_file_from_yaml()['password_page']['_location'])   # 获取安全键盘的定位
        keyboard_height = keyboard_size.size['height']  # 获取安全键盘的高
        keyboard_width = keyboard_size.size['width']   # 获取安全键盘的宽
        start_x = keyboard_size.location['x']
        start_y = keyboard_size.location['y']
        for num in pwd:   # 根据输入的交易密码，点击安全键盘
            if int(num) == 1:
                self.tap(start_x + keyboard_width / 6, start_y + keyboard_height / 8)
            elif int(num) == 2:
                self.tap(start_x + keyboard_width / 2, start_y + keyboard_height / 8)
            elif int(num) == 3:
                self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height / 8)
            elif int(num) == 4:
                self.tap(start_x + keyboard_width / 6, start_y + keyboard_height * 3 / 8)
            elif int(num) == 5:
                self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 3 / 8)
            elif int(num) == 6:
                self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 3 / 8)
            elif int(num) == 7:
                self.tap(start_x + keyboard_width / 6, start_y + keyboard_height * 5 / 8)
            elif int(num) == 8:
                self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 5 / 8)
            elif int(num) == 9:
                self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 5 / 8)
            elif int(num) == 0:
                self.tap(start_x + keyboard_width /2, start_y + keyboard_height * 7 / 8)

        # self.tap(start_x + keyboard_width / 6, start_y + keyboard_height / 8)
        # self.tap(start_x + keyboard_width / 2, start_y + keyboard_height / 8)
        # self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 3 / 8)
        # self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 3 / 8)
        # self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 3 / 8)
        # self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 3 / 8)



