import logging
import time
import unittest
from appium_function.init_driver import init_driver
from pages.devices_connection_page import DeviceConnectionPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class BG5SConnection(unittest.TestCase):
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
        self.homePage = HomePage(self.driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)

    def test_login(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        self.homePage.click_mac_name()
        # for i in range(500):
        #     self.homePage.click_mac_name()
        #     time.sleep(10)
        #     self.deviceConnectionPage.click_close_button()
        #     time.sleep(2)

    def tearDown(self):
        pass
        print("=============Test End=============")


if __name__ == '__main__':
    unittest.main()
