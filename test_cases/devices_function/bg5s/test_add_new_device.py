import logging_module
import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from appium_function.init_driver import init_driver
from common.common_step import CommonStep
from pages.devices_connection_page import DeviceConnectionPage
from pages.app_home_page import HomePage
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.setup_guide_page import SetupGuidePage


class AddNewDevice(unittest.TestCase):
    log = logging_module.getLogger(__name__)

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

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
        self.productListPage = ProductListPage(self.driver)
        self.setupGuidePage = SetupGuidePage(self.driver)
        self.commonFunction = CommonStep(self.driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)

    def tearDown(self):
        print("=============Test End=============")
        self.commonFunction.disconnected_devices('Gluco+-267328')

    def test_add_new_device(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        time.sleep(3)
        # 检查是否已经绑定过该设备，绑定过就解绑
        self.commonFunction.disconnected_devices('Gluco+-267328')
        # 添加BG5S设备
        self.homePage.click_add_button()
        self.productListPage.add_bg5s('5C0272267328')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(
            'com.ihealthlabs.MyVitalsPro:id/tv_bg_connect_title'))
        actual = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_bg_connect_title').text
        expect = "The device is connected."
        self.assertEqual(actual, expect, '设备连接成功')
        self.deviceConnectionPage.click_close_button()


if __name__ == '__main__':
    unittest.main()
