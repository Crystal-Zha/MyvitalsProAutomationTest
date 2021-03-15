import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appium_function.element_function import BaseFun
from pages.devices_connection_page import DeviceConnectionPage
from pages.setup_guide_page import SetupGuidePage


class ProductListPage(BaseFun):
    # 血压仪
    blood_pressure_monitors_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_select_bp')
    # 体重秤
    scales_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_select_hs')
    # 血糖仪
    blood_glucose_meter_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_select_bg')
    # 血氧仪
    pulse_oximeter_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_select_po')
    # 体温枪
    thermometer_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_select_th')

    # 血糖仪各型号
    bg1_loc = 'Align(BG1)'
    bg5_loc = 'Smart(BG5)'
    bg5s_loc = 'Gluco+(BG5S)'

    def __init__(self, driver):
        super().__init__(driver)
        self.setupGuidePage = SetupGuidePage(self.driver)
        self.deviceConnectionPage = DeviceConnectionPage(self.driver)

    def click_blood_pressure_monitors(self):
        self.click(self.blood_glucose_meter_loc)

    def click_scales(self):
        self.click(self.scales_loc)

    def click_blood_glucose_meter(self):
        self.click(self.blood_glucose_meter_loc)

    def click_pulse_oximeter(self):
        self.click(self.pulse_oximeter_loc)

    def click_thermometer(self):
        self.click(self.thermometer_loc)

    def click_allow_permission(self):
        self.driver.find_element_by_id(
            'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

    def choose_bg5(self):
        self.click_blood_glucose_meter()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % self.bg5_loc).click()
        time.sleep(2)
        if BaseFun.is_element_exist(self, "仅在使用此应用时允许"):
            self.driver.find_element_by_id(
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            time.sleep(2)
        else:
            return

    '''
    添加BG5S设备
    '''
    def add_bg5s(self, mac_name):
        self.click_blood_glucose_meter()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % self.bg5s_loc).click()
        time.sleep(2)
        if BaseFun.is_element_exist(self, "仅在使用此应用时允许"):
            self.driver.find_element_by_id(
                "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
            time.sleep(2)
        else:
            return
        self.setupGuidePage.click_next_button()
        time.sleep(8)
        self.setupGuidePage.select_device_for_your_mac_name(mac_name)

    def choose_bg1(self):
        self.click_blood_glucose_meter()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % self.bg1_loc).click()
        time.sleep(2)
        if BaseFun.is_element_exist(self, "允许"):
            self.driver.find_element_by_id(
                "com.android.permissioncontroller:id/permission_allow_button").click()
            time.sleep(2)
        else:
            return
