from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun

'''
这个页面是封装设备信息界面所有的元素以及操作步骤
'''


class DeviceInfoPage(BaseFun):
    # 设备的mac地址
    device_id_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_device_id')
    # 固件版本
    hardware_version_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_hardware_version')
    # 软件版本
    firmware_version_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_firmware_version')
    # 电量
    battery_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_battery')
    # 质控液
    control_solution_testing_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_control_solution_testing')
    # forgot it
    forgot_it_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/device_details_forgot_it')

    # 解绑弹框
    # 文本
    comfirm_message = (By.NAME, 'The device will be deleted from your account. Are you sure?')
    # ok
    ok_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_right')
    # cancel
    cancel_loc = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/tv_left')

    def click_forgor_it_button(self):
        self.click(self.forgot_it_loc)

    def click_ok(self):
        self.click(self.ok_loc)

    def disconnected_device(self):
        self.click_forgor_it_button()
        self.click_ok()
