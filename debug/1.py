import time
from appium import webdriver
from util.get_by_local import GetByLocal
from log.user_log import UserLog
from business.mine_business import MineBusiness

log = UserLog()
logger = log.get_logger()


class TestStart:
    def __init__(self):

        self.driver = self.get_driver()
        self.get_by_local = GetByLocal(self.driver)

    def get_driver(self):
        """获取driver"""
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "192.168.56.101:5555",
            # "deviceName": "ac05b72c",
            # "app": "../data/JZB_7.0.8-website-release.apk",
            "app": "/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/data/JZB_7.0.8-website-release.apk",
            # "appWaitActivity": "com.eduu.bang.app.SplashActivity",  # 需要等待切换activity(真机常见问题)
            "noReset": "true",  # 不用每次启动都重置应用
            "unicodeKeyboard": "true",  # 使用unicode编码方式发送字符串
            "resetKeyboard": "true"  # 是否重置键盘
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        time.sleep(5)
        return driver

    def aa(self):
        try:
            a = self.get_by_local.isElementExist('mine_element1', 'mine_tab')
            if a == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
            a = False
        finally:
            log.close_handle()
        return a

    def quit(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    t = TestStart()
    m = MineBusiness()
    print(t.aa())
    t.quit()
