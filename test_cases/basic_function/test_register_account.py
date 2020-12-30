import logging
import unittest

import common

from appium_function.init_driver import init_driver
from common.common_function import CommonFun
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class RegisterAccounr(unittest.TestCase):
    log = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        driver = init_driver()
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print("=============Test Start=============")
        self.loginPage = LoginPage(self.driver)
        self.settingPage = SettingPage(self.driver)

    def test_password_not_match(self):
        self.loginPage.click_register_account()
        self.loginPage.input_register_email()
        print("前后密码输入不匹配")
        self.loginPage.input_first_password('123456')
        self.loginPage.input_comfirm_password('123456')
        self.loginPage.click_check_box()
        self.loginPage.click_next_button()

    def test_register_new_account(self):
        print("=============注册新用户=============")
        self.loginPage.click_register_account()
        self.loginPage.input_register_email()
        print("前后密码输入不匹配")
        self.loginPage.input_first_password('123456')
        self.loginPage.input_comfirm_password('123456')
        self.loginPage.click_check_box()
        self.loginPage.click_next_button()

        self.loginPage.select_female()
        self.loginPage.select_born()
        self.loginPage.click_next_button()
        self.loginPage.click_check_box()
        self.loginPage.click_ok()

    def test_register_exit_account(self):
        self.loginPage.click_register_account()
        self.loginPage.input_register_email()

    def tearDown(self):
        print("=============Test End=============")


if __name__ == '__main__':
    unittest.main()
