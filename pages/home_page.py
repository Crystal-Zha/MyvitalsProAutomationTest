import uiautomator2 as u2
from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class HomePage(BaseFun):
    # mac地址为Gluco+-0E64B4的设备
    bg5s_device_name = 'Gluco+-0E64B4'
    my_devices_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_my_devices')

    def click_mac_name(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % self.bg5s_device_name).click()
