import time
import unittest

import logging_module

from selenium.webdriver.support.wait import WebDriverWait

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class Units_Function(unittest.TestCase):
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

    def test_goals_function(self):
        self.loginPage.login_to_home_page('test003@gmail.com', '123456')
        self.settingPage.click_setting()
        self.settingPage.click_glucose_range()
        time.sleep(2)
        actual = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_before_low').text
        expect = '80'
        self.assertEqual(actual, expect, '相等')
        self.settingPage.click_save_glucose_range()
        self.settingPage.click_units()
        self.settingPage.select_glucose_unit_to_mmolL()
        self.settingPage.save_units_loc()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_units'))

        # 查看单位是否正常切换
        self.settingPage.click_glucose_range()
        actual1 = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/ed_before_low').text
        expect1 = '4.4'
        self.assertEqual(actual1, expect1, '单位切换成功')
        self.settingPage.click_save_glucose_range()

        self.settingPage.click_units()
        self.settingPage.select_gluocose_unit_to_mmdlL()
        self.settingPage.save_units_loc()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_units'))

    def tearDown(self):
        print("=============Test End=============")
        self.settingPage.logout()


if __name__ == '__main__':
    unittest.main()