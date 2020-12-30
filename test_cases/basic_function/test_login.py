import logging
import unittest

from nose.tools import *

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class Login(unittest.TestCase):
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

    def test_login(self):
        print("=============test_login Start=============")
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')

    def tearDown(self):
        self.settingPage.logout()
        print("=============Test End=============")


if __name__ == '__main__':
    unittest.main()
