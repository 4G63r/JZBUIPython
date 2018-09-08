import time
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class ActionMethod:
    def __init__(self):
        self.driver = BaseDriver().android_driver(0)
        self.get_by_local = GetByLocal(self.driver)

    def input(self, section, key, value):
        """元素输入"""
        element = self.get_by_local.get_element(section, key)
        if element == None:
            return str(section) + " or " + str(key) + "元素未找到❗❗❗️"
        element.send_keys(value)

    def on_click(self, section, key):
        """元素点击"""
        element = self.get_by_local.get_element(section, key)
        if element == None:
            return str(section) + " or " + str(key) + "元素未找到❗❗❗️"
        element.click()

    def sleep_time(self, value):
        """等待时长"""
        time.sleep(value)

    def get_size(self):
        """获取屏幕宽和高"""
        size = self.driver.get_window_size()  # 返回字典{'height': 2560, 'width': 1440}
        height = size['height']  # y
        width = size['width']  # x
        return width, height  # 返回元祖(1440, 2560)

    def swipe_left(self):
        """向左滑动"""
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    def swipe_right(self):
        """向右滑动"""
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1)

    def swipe_up(self):
        """向上滑动"""
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)

    def swipe_down(self):
        """向下滑动"""
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self, direction):
        """滑动封装"""
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()


if __name__ == '__main__':
    a = ActionMethod()
    a.input('ad', 'da', '123')
