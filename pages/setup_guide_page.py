import time
from telnetlib import EC

from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class SetupGuidePage(BaseFun):
    next_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/btn_next')
    back_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_back')

    select_the_device_to_connect = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/header')
    cancel = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/footer')

    def click_next_button(self):
        self.click(self.next_loc)

    def select_device_for_your_mac_name(self, mac_name):
        while True:
            try:
                if BaseFun.is_element_exist(self, mac_name):
                    self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % mac_name).click()
                    break
                else:
                    self.driver.swipe(668, 1188, 668, 1140)

            except Exception as e:
                return print('没找到元素')






