import time

from selenium.common.exceptions import NoSuchElementException
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

    # 重写获取文本的方法
    # def get_text(self):
    #

    # 重写click方法
    def click(self, loc):
        element = self.find_element(loc)
        element.click()

    # 封装长按方法
    def long_press(self, x1, y1, te):
        TouchAction(self.driver).long_press(x=x1, y=y1).wait(te).release().perform()

    # 封装滑动查找元素
    def find_by_scroll(self, item_name):
        item = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector('
            ').className("android.widget.TextView"), " '
            + item_name + '")')
        item.click()

    # 判断元素是否存在
    # def is_exist(self, element):
    #     if (self.driver.find_element(By.xpath（“ // * [@ text ='Allow']”].isDisplayed()))

    #  封装滑动的方法
    # 1.向上滑动
    def swip_up(self, time=1000):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.25
        y2 = l['height'] * 0.75
        self.driver.swipe(x1, y1, x1, y2, time)

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
        # TouchAction(self.driver).press(x=x1, y=y1).move_to(x2, y2).release().perform()

    # /判断元素是否存在
    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag

    def is_element_exist(self, element):
        source = self.driver.page_source
        print(source)
        if element in source:
            return True
        else:
            return False
