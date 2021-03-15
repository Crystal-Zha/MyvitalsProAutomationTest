import logging_module
import time
import unittest
import random

from selenium.webdriver.support.select import Select

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class AccountInfoFunction(unittest.TestCase):
    driver = None
    log = logging_module.getLogger(__name__)

    @classmethod
    def setUpClass(cls):
        driver = init_driver()
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.quit()

    def setUp(self):
        print("=============Test Start=============")
        self.loginPage = LoginPage(self.driver)
        self.settingPage = SettingPage(self.driver)

    def test_account_function(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        self.settingPage.click_setting()
        self.settingPage.enter_to_user_info_button()

        # 检查UI
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/setting_iv_head')
        actual1 = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_account').text
        expect = 'test003@gmail.com'
        self.assertEqual(actual1, expect, '断言成功')
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_user_height')
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_user_weight')
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_user_birthdate')
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_user_gender')

        # 修改账户名
        self.settingPage.change_user_name('哈哈哈')
        time.sleep(3)

        # 选择性别
        self.settingPage.click_gender()
        self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/btnSubmit').click()

        # 选择日期
        self.settingPage.click_birthday()
        self.settingPage.click_done()

        # 选择身高
        self.settingPage.click_height()
        self.settingPage.click_done()

        # 选择体重
        self.settingPage.click_weight()
        num = random.randint(0, 10)
        Select(self.driver.find_element_by_id("com.ihealthlabs.MyVitalsPro:id/wv_weight_first_lb")).select_by_value(num)
        Select(self.driver.find_element_by_id("com.ihealthlabs.MyVitalsPro:id/wv_weight_second")).select_by_value(num)
        Select(self.driver.find_element_by_id("com.ihealthlabs.MyVitalsPro:id/wv_weight_third")).select_by_value(num)
        Select(self.driver.find_element_by_id("com.ihealthlabs.MyVitalsPro:id/wv_weight_fourth")).select_by_value(num)
        self.settingPage.click_done()

