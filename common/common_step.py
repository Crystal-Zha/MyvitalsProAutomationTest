import time
from appium_function.element_function import BaseFun
from pages.device_info_page import DeviceInfoPage
from pages.devices_connection_page import DeviceConnectionPage


class CommonStep(BaseFun):

    def __init__(self, driver):
        super().__init__(driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)
        self.deviceInfoPage = DeviceInfoPage(self.driver)

    def disconnected_devices(self, exist_mac_name):
        if BaseFun.is_element_exist(self, exist_mac_name):
            print("元素存在")
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % exist_mac_name).click()
            if BaseFun.is_element_exist(self, "仅在使用此应用时允许"):
                self.driver.find_element_by_id(
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
                time.sleep(2)
            time.sleep(5)
            self.deviceConnectionPage.click_device_setting_button()
            self.deviceInfoPage.disconnected_device()
        else:
            print("元素不存在")



