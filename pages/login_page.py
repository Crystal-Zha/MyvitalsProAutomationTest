# -*- coding: UTF-8 -*-
"""
这个page是编写登录界面所有元素以及页面常用的操作场景
"""
import time

from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun
from common.common_function import CommonFun


class LoginPage(BaseFun):
    """
    登录页面
    """

    # 用户名输入框
    user_name_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_user_name')
    # 密码输入框
    password_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_user_password')
    # 登录按钮
    loginButton_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_login')
    # 忘记密码
    forgot_password_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_forgot_password')
    # 创建新账号
    register_account_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_register')

    # 登录失败提示
    password_error_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_message')
    # ok按钮
    ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_left')


    '''
    以下是这个页面用到的操作步骤
    '''
    def click_user_name(self):
        self.click(self.user_name_loc)

    def input_user_name(self, email):
        self.send_keys(self.user_name_loc, email)

    def click_password(self):
        self.click(self.password_loc)

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    def click_login(self):
        self.click(self.loginButton_loc)

    # 点击创建账号按钮
    def click_register_account(self):
        self.click(self.register_account_loc)

    def click_ok_button(self):
        self.click(self.ok_loc)

    def login_to_home_page(self, username, password):
        self.click_user_name()
        self.input_user_name(username)
        self.click_password()
        self.input_password(password)
        self.click_login()
        time.sleep(5)



    # 获取密码输入不匹配提示
    # def get_password_not_match_text(self):
