import logging_module
import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from appium_function.init_driver import init_driver
from pages.devices_connection_page import DeviceConnectionPage
from pages.app_home_page import HomePage
from pages.login_page import LoginPage


class BG5SConnection(unittest.TestCase):
    log = logging_module.getLogger(__name__)

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
        self.homePage = HomePage(self.driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)

    def test_login(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        self.homePage.click_exist_bg5s_mac_name('Gluco+-267328', '5C0272267328')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(
            'com.ihealthlabs.MyVitalsPro:id/tv_bg_connect_title'))
        actual = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_bg_connect_title').text
        expect = "The device is connected."
        self.assertEqual(actual, expect, '设备连接成功')
        self.deviceConnectionPage.click_close_button()
        time.sleep(2)

    def tearDown(self):
        pass
        print("=============Test End=============")


if __name__ == '__main__':
    unittest.main()
