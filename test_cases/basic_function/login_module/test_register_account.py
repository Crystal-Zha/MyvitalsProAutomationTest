import logging
import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.setting_page import SettingPage


class RegisterAccount(unittest.TestCase):
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
        self.registerPage = RegisterPage(self.driver)
        self.settingPage = SettingPage(self.driver)

    def test_register_new_account_fail(self):
        self.loginPage.click_register_account()
        # 获取随机邮箱
        self.registerPage.input_random_register_email()
        print("======测试场景一 ：输入密码前后不匹配======")
        self.registerPage.input_first_password('123456')
        self.registerPage.input_comfirm_password('1234567')
        # self.registerPage.click_check_box()
        self.registerPage.click_next_button()
        time.sleep(2)
        actual1 = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_register_input_error_info').text
        expect = "Password does not match, please re-enter"
        self.assertEqual(actual1, expect, '密码不匹配')
        self.registerPage.click_back()

        print("======测试场景二 ：输入密码长度不符合要求======")
        self.loginPage.click_register_account()
        self.registerPage.input_random_register_email()
        self.registerPage.input_first_password('1234')
        self.registerPage.input_comfirm_password('1234')
        # self.registerPage.click_check_box()
        self.registerPage.click_next_button()
        time.sleep(2)
        actual2 = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_register_input_error_info').text
        expect = "Password must be between 6–128 characters"
        self.assertEqual(actual2, expect, '密码长度不符合要求')
        self.registerPage.click_back()

        print("======测试场景三 ：输入邮箱不符合要求======")
        self.loginPage.click_register_account()
        self.registerPage.input_register_email('??@gmail.com')
        self.registerPage.input_first_password('123456')
        self.registerPage.input_comfirm_password('123456')
        # self.registerPage.click_check_box()
        self.registerPage.click_next_button()
        time.sleep(2)
        actual3 = self.driver.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_register_input_error_info').text
        expect = "Please enter a valid email address"
        self.assertEqual(actual3, expect, '邮箱无效')
        self.registerPage.click_back()

    def test_register_new_account_success(self):
        self.loginPage.click_register_account()
        self.registerPage.input_random_register_email()
        self.registerPage.input_first_password('123456')
        self.registerPage.input_comfirm_password('123456')
        # self.registerPage.click_check_box()
        self.registerPage.click_next_button()
        self.registerPage.select_female()
        self.registerPage.select_born()
        self.registerPage.click_next_button()
        self.registerPage.click_check_box()
        self.registerPage.click_ok()
        # 等待app主页出现
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('com.ihealthlabs.MyVitalsPro:id/tv_my_devices'))
        self.settingPage.logout()

    def tearDown(self):
        print("=============Test End=============")
        pass


if __name__ == '__main__':
    unittest.main()
