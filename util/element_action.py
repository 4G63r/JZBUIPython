import time
from log.print_log import Log

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "


class ElementAction:
    """元素所有行为操作"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, el):
        """点击操作"""
        start_t = time.time()
        try:
            el[1].click()
            logger.info(
                "{0} Clicked element: <{1}>, Spend {2} seconds".format(success, el[0], round(time.time() - start_t, 2)))
        except Exception:
            logger.info(
                "{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, el[0],
                                                                               round(time.time() - start_t, 2)))
            raise

    def clear_input(self, el, text):
        """清空后输入内容"""
        start_t = time.time()
        try:
            el[1].clear()
            el[1].send_keys(text)
            logger.info(
                "{0} Clear and input element: <{1}> content: {2}, Spend {3} seconds".format(success, el[0], text,
                                                                                            round(time.time() - start_t,
                                                                                                  2)))
        except Exception:
            logger.info(
                "{0} Unable to clear and input element: <{1}> content: {2}, Spend {3} seconds".format(fail, el[0], text,
                                                                                                      round(
                                                                                                          time.time() - start_t,
                                                                                                          2)))
            raise

    def input(self, el, text):
        """输入内容"""
        start_t = time.time()
        try:
            el[1].send_keys(text)
            logger.info("{0} Input element: <{1}> content: {2}, Spend {3} seconds".format(success, el[0], text,
                                                                                          round(time.time() - start_t,
                                                                                                2)))
        except Exception:
            logger.info("{0} Unable to input element: <{1}> content: {2}, Spend {3} seconds".format(fail, el[0], text,
                                                                                                    round(
                                                                                                        time.time() - start_t,
                                                                                                        2)))
            raise

    def get_text(self, el):
        """获取文案"""
        start_t = time.time()
        try:
            text = el[1].text
            logger.info(
                "{0} Get element <{1}> text: <{2}>, Spend {3} seconds".format(success, el[0], text,
                                                                              round(time.time() - start_t, 2)))
            return text
        except Exception:
            logger.info(
                "{0} Unable to get element <{1}> text, Spend {2} seconds".format(fail, el[0],
                                                                                 round(time.time() - start_t, 2)))
            raise

    def quit(self):
        """退出driver"""
        start_t = time.time()
        self.driver.quit()
        logger.info(
            "{0} Closed all window and quit the driver, Spend {1} seconds".format(success,
                                                                                  round(time.time() - start_t, 2)))

    def element_exist(self, el):
        """判断元素是否存在"""
        start_t = time.time()
        try:
            el[1]
            logger.info("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, el[0],
                                                                                round(time.time() - start_t, 2)))
            return True
        except Exception:
            logger.info("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, el[0],
                                                                                    round(time.time() - start_t, 2)))
            return False

    def take_screenshot(self, file_path):
        """截图"""
        start_t = time.time()
        try:
            self.driver.save_screenshot(file_path)
            logger.info("{0} Get the current window screenshot, path: {1}, Spend {2} seconds".format(success, file_path,
                                                                                                     round(
                                                                                                         time.time() - start_t,
                                                                                                         2)))
        except Exception:
            logger.info(
                "{0} Unable to get the current window screenshot, path: {1}, Spend {2} seconds".format(fail, file_path,
                                                                                                       round(
                                                                                                           time.time() - start_t,
                                                                                                           2)))
            raise

    def sleep(self, value):
        """固定时长"""
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
        if direction.lower() == 'up':
            self.swipe_up()
        elif direction.lower() == 'down':
            self.swipe_down()
        elif direction.lower() == 'left':
            self.swipe_left()
        elif direction.lower() == 'right':
            self.swipe_right()

    def js(self, script):
        """执行JavaScript"""
        start_t = time.time()
        try:
            self.driver.execute_script(script)
            logger.info(
                "{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script,
                                                                                round(time.time() - start_t, 2)))
        except Exception:
            logger.info("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail, script,
                                                                                                  round(
                                                                                                      time.time() - start_t,
                                                                                                      2)))
            raise

    def get_attribute(self, el, attribute):
        """获取属性值"""
        start_t = time.time()
        try:
            attr = el[1].get_attribute(attribute)
            logger.info(
                "{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success, el[0], attribute,
                                                                                            round(time.time() - start_t,
                                                                                                  2)))
            return attr
        except Exception:
            logger.info(
                "{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail, el[0],
                                                                                                      attribute,
                                                                                                      round(
                                                                                                          time.time() - start_t,
                                                                                                          2)))
            raise
