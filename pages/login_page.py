# -*- coding: UTF-8 -*-
"""
这个page是编写登录界面常用的操作场景
"""
import time

from appium_function.element_function import BaseFun


class LoginPage(BaseFun):
    """
    登录
    """
    def login_to_home_page(self, username, password):
        self.driver.find_element_by_id(user_name).click()

        self.input_user_name(username)
        self.click_password()
        self.input_password(password)
        self.click_login()
        time.sleep(5)

    # 获取密码输入不匹配提示
    # def get_password_not_match_text(self):
