import logging_module
import unittest

from appium_function.init_driver import init_driver
from pages.login_page import LoginPage
from pages.setting_page import SettingPage


class GoalsFunction(unittest.TestCase):
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
        self.settingPage.click_goals()
        self.settingPage.input_target_weight()

    def tearDown(self):
        print("=============Test End=============")
        self.settingPage.logout()


if __name__ == '__main__':
    unittest.main()
