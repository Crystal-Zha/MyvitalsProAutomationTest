import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appium_function.element_function import BaseFun
from pages.devices_connection_page import DeviceConnectionPage
from pages.product_list_page import ProductListPage


class HomePage(BaseFun):

    my_devices_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_my_devices')
    select_new_device_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_add_device')
    add_button_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_add_device')

    def __init__(self, driver):
        super().__init__(driver)
        self.productListPage = ProductListPage(self.driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)

    def click_select_new_device(self):
        self.click(self.select_new_device_loc)

    def click_add_button(self):
        self.click(self.add_button_loc)

    def disconnecting_device(self):
        self.driver.keyevent(4)

    def click_exist_bg5s_mac_name(self, exist_mac_name, mac_name):
        if BaseFun.is_element_exist(self, exist_mac_name):
            print("元素存在")
        else:
            self.click_add_button()
            self.productListPage.add_bg5s(mac_name)
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(
                'com.ihealthlabs.MyVitalsPro:id/tv_bg_connect_title'))
            self.deviceConnectionPage.click_close_button()
            time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % exist_mac_name).click()
        if BaseFun.is_element_exist(self, "仅在使用此应用时允许"):
            self.driver.find_element_by_id(
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            time.sleep(2)
        time.sleep(10)
