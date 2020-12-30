import time

from appium import webdriver


def init_driver():
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    # 设备号
    desired_caps['deviceName'] = 'R5CNA08QTSV'
    # desired_caps['deviceName'] = 'UYT0217A10002648'
    # 包名
    desired_caps['appPackage'] = 'com.ihealthlabs.MyVitalsPro'
    # Activity
    desired_caps['appActivity'] = 'com.ihealth.business.common.welcome.WelcomeActivity'

    desired_caps['autoAcceptAlerts'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 将driver对象返回
    return driver


if __name__ == '__main__':
    driver = init_driver()
    time.sleep(10)
