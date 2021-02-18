import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class InputPassword(BasePage):   # 交易密码
    @allure.step("输入交易密码")
    def input_password(self):    # 输入交易密码

        keyboard_size = self.find_element(By.ID, self.get_file_from_yaml()['password_page']['_location'])
        keyboard_height = keyboard_size.size['height']
        keyboard_width = keyboard_size.size['width']
        start_x = keyboard_size.location['x']
        start_y = keyboard_size.location['y']
        self.tap(start_x + keyboard_width / 6, start_y + keyboard_height / 8)
        self.tap(start_x + keyboard_width / 2, start_y + keyboard_height / 8)
        self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 3 / 8)
        self.tap(start_x + keyboard_width / 2, start_y + keyboard_height * 3 / 8)
        self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 3 / 8)
        self.tap(start_x + keyboard_width * 5 / 6, start_y + keyboard_height * 3 / 8)



