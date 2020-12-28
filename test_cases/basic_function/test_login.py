import logging
import unittest

import nose
from nose.tools import *

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage


class Login(unittest.TestCase):
    log = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        driver = init_driver()
        cls.driver = driver

    def setUp(self):
        self.loginPage = LoginPage(self.driver)
        print("=============Test Start=============")

    @nose.allure.feature('登录')
    @nose.allure.story('登录')
    def test_Login(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')

    def tearDown(self):
        pass
        print("=============Test End=============")

    @classmethod
    def tearDownClass(cls):
    #     cls.diver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
