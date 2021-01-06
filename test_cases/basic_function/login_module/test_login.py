import logging
import time
import unittest

from nose.tools import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appium_function.init_driver import init_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class Login(unittest.TestCase):
    driver = None
    log = logging.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        driver = init_driver()
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("=============Test Start=============")
        self.loginPage = LoginPage(self.driver)
        self.settingPage = SettingPage(self.driver)
        self.homePage = HomePage(self.driver)

    def test_login_fail(self):
        print("=============test_login Start=============")
        self.loginPage.login_to_home_page('test003@gmail.com', '1234567')
        time.sleep(5)
        # 等待错误弹框出现
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_message'))
        self.loginPage.click_ok_button()
        time.sleep(2)
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/et_user_name').clear()
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/et_user_password').clear()

    def test_login_success(self):
        print("=============test_login Start=============")
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        time.sleep(5)
        actual = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_my_devices').text
        expect = "My Devices"
        self.assertEqual(actual, expect, '成功登陆')
        self.settingPage.logout()

    def tearDown(self):
        print("=============Test End=============")
        pass


if __name__ == '__main__':
    unittest.main()
