import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction


class BaseFun(object):

    def __init__(self, driver):
        self.driver = driver

    # 二次封装find_element方法
    def find_element(self, loc, timeout=10):
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(loc))
        return element

    # 重写clear方法
    def clear(self, loc):
        self.find_element(loc).clear()

    # 重写sendKeys方法
    def send_keys(self, loc, value):
        element = self.find_element(loc)
        element.clear()
        element.send_keys(value)

    # 重写click方法
    def click(self, loc):
        element = self.find_element(loc)
        element.click()

    # 封装长按方法
    def long_press(self, x1, y1, te):
        TouchAction(self.driver).long_press(x=x1, y=y1).wait(te).release().perform()

    # 封装滑动的方法
    # 1.向上滑动
    def swip_up(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.75, x * 0.5, y * 0.25, time)

    # 2.向下滑动
    def swip_down(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.25, x * 0.5, y * 0.75, time)

    # 3.向左滑动
    def swip_left(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.25, y * 0.5, time)

    # 4.向右滑动
    def swip_right(self, time=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.25, y * 0.5, x * 0.75, y * 0.5, time)

    # 拖动
    def move(self, x1, y1, x2, y2):
        TouchAction(self.driver).long_press(x=x1, y=y1).move_to(x2, y2).release().perform()

    # 判断控件是否存在
    def isExit(self, loc):
        if self.find_element(loc) == 0:
            print(0)
            return 0
        else:
            print(1)
            return 1




