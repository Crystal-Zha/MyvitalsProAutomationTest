# -*- coding: UTF-8 -*-
"""
这个page是编写登录界面所有元素，包括注册，以及页面常用的操作场景
"""
import time

from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class LoginPage(BaseFun):

    # 邮箱输入框
    email_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_user_name')
    # 密码输入框
    password_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_user_password')
    # 登录按钮
    loginButton_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_login')


    '''
    以下是这个页面用到的操作步骤
    '''

    def click_email(self):
        self.click(self.email_loc)

    def input_email(self, email):
        self.send_keys(self.email_loc, email)

    def click_password(self):
        self.click(self.password_loc)

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    def click_login(self):
        self.click(self.loginButton_loc)

    def login_to_home_page(self, email, password):
        self.click_email()
        self.input_email(email)
        self.click_password()
        self.input_password(password)
        self.click_login()
        time.sleep(5)
