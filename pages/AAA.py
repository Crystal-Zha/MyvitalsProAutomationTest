from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class IHealthDriver:
    def __init__(self):
        # appium服务监听地址
        server='http://localhost:4723/wd/hub'
        # app启动参数
        desired_caps={'platformName': 'Android',
                    'platformVersion': '10',
                    'deviceName': 'R5CNA08QTSV',
                    'appPackage': 'com.ihealthlabs.MyVitalsPro',
                    'appActivity': 'com.ihealth.business.common.welcome.WelcomeActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True
        }
        # 驱动
        self.driver = webdriver.Remote(server,desired_caps)
        self.wait = WebDriverWait(self.driver,30)
# 获取登录按钮
email_et = IHealthDriver().wait.until(EC.presence_of_element_located((By.ID,'com.ihealthlabs.MyVitalsPro:id/et_user_name')))
# 点击登录按钮
email_et.click()
# 填写手机号文本框
email_et.send_keys("18888888888")