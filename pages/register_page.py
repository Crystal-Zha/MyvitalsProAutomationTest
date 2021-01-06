# -*- coding: UTF-8 -*-
"""
这个page是编写注册账户界面所有元素以及页面常用的操作场景
"""
from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun
from common.common_function import CommonFun


class RegisterPage(BaseFun):
    '''
    注册账号
    '''
    #返回按钮
    back_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_back')
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
    # 年份选择框的done按钮
    done_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btnSubmit')
    # OK
    ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_create_account_done')

    '''
    警告提示内容
    '''
    password_error = 'com.ihealthlabs.MyVitalsPro:id/tv_register_input_error_info'

    # 邮箱无效
    # 'Please enter a valid email address'

    # 密码输入不符合要求提示
    # 'Password must be between 6–128 characters'

    # 前后密码输入不匹配提示
    # 'Password does not match, please re-enter'


    # 点击返回按钮
    def click_back(self):
        self.click(self.back_loc)

    # 输入邮箱
    def input_register_email(self, register_email):
        self.click(self.register_email_loc)
        self.send_keys(self.register_email_loc, register_email)

    # 注册随机邮箱
    def input_random_register_email(self):
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

    # 点击生日
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

    # 选择出生日期
    def select_born(self):
        self.click_birthday()
        self.click(self.done_loc)
