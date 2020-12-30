# -*- coding: UTF-8 -*-
"""
这个page是编写登录界面所有元素，包括注册，以及页面常用的操作场景
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

    '''
    注册账号
    '''
    # email
    register_email_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_email')
    # 第一次密码输入框
    first_password_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_password')
    # 确认密码输入框
    comfirm_password_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/et_password_confirm')
    # 阅读协议复选框
    check_box_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/policy_checked')
    # 下一步
    next_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_next')

    # 女性
    female_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_female')
    # 男性
    male_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_male')
    # 生日
    birthday_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/ed_birthday')
    #年份选择框的done按钮
    done_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btnSubmit')
    # OK
    ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_create_account_done')

    '''
    警告提示内容
    '''
    #密码输入不符合要求提示
    password_error = (By.NAME, 'Password must be between 6–128 characters')

    #前后密码输入不匹配提示
    password_not_match = (By.NAME, 'Password does not match, please re-enter')

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

    # 输入注册邮箱
    def input_register_email(self):
        self.click(self.register_email_loc)
        register_email = CommonFun().email
        self.send_keys(self.register_email_loc, register_email)

    def input_first_password(self, password1):
        self.click(self.first_password_loc)
        self.send_keys(self.first_password_loc, password1)

    def input_comfirm_password(self, password2):
        self.click(self.comfirm_password_loc)
        self.send_keys(self.comfirm_password_loc, password2)

    # 勾选协议复选框
    def click_check_box(self):
        self.click(self.check_box_loc)

    # 下一步
    def click_next_button(self):
        self.click(self.next_loc)

    #点击生日
    def click_birthday(self):
        self.click(self.birthday_loc)

    # 选择性别女
    def select_female(self):
        self.click(self.female_loc)

    # 选择性别男
    def select_male(self):
        self.click(self.male_loc)

    # 点击ok
    def click_ok(self):
        self.click(self.ok_loc)

    def login_to_home_page(self, username, password):
        self.click_user_name()
        self.input_user_name(username)
        self.click_password()
        self.input_password(password)
        self.click_login()
        time.sleep(5)

    # 选择出生日期
    def select_born(self):
        self.click_birthday()
        self.click(self.done_loc)

    # 获取密码输入不匹配提示
    # def get_password_not_match_text(self):







