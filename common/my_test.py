# coding=utf-8

import unittest
import warnings

from appium_function.init_driver import init_driver
from common.log import Log
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.setting_page import SettingPage


class MyTest(unittest.TestCase):
    """
    适用于所有的testcase
    """

    def setUp(self):
        self.logger = Log()
        self.logger.info('#####################  START  ######################')
        warnings.simplefilter('ignore', ResourceWarning)
        driver = init_driver()
        self.driver = driver
        self.loginPage = LoginPage(self.driver)
        self.registerPage = RegisterPage(self.driver)
        self.settingPage = SettingPage(self.driver)

    def tearDown(self):
        self.driver.quit()
        self.logger.info("#######################  END  #####################")
