# -*- coding: UTF-8 -*-

"""
这个page是编写account界面所有的元素以及常用的操作
"""
from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class SettingPage(BaseFun):
    # 主页设置按钮
    setting_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_settings')

    # 主页设备按钮
    device_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_devices')

    # 主页趋势图
    summary_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_trends')


    '''
        登出
    '''
    # 登出
    logout_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/log_out')

    # 确认框文本
    message_loc = (By.NAME, 'Are you sure you want to log out？')

    # 确认框ok按钮
    dialog_ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_right')

    # cancel
    dialog_cancel_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_left')

    def click_setting(self):
        self.click(self.setting_loc)

    def click_logout(self):
        self.click(self.logout_loc)

    def click_ok(self):
        self.click(self.dialog_ok_loc)

    def click_cancel(self):
        self.click(self.dialog_cancel_loc)

    # 登出
    def logout(self):
        self.click_setting()
        self.click_logout()
        self.click_ok()


