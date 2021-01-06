from selenium.webdriver.common.by import By

from appium_function.element_function import BaseFun


class DeviceConnectionPage(BaseFun):
    # 关闭按钮
    close_button = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_back')
    # 设置按钮
    device_setting_button = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/iv_right')
    # 历史数据
    history_button = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_history_btn')
    # 离线数据上传
    sync_button = (By.ID, 'com.ihealthlabs.MyVitalsPro:id/rl_update_offline')

    def click_close_button(self):
        self.click(self.close_button)

    def click_device_setting_button(self):
        self.click(self.device_setting_button)

    def click_history_button(self):
        self.click(self.history_button)

    def click_sync_button(self):
        self.click(self.sync_button)
