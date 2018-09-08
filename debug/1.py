import time

from appium import webdriver


def get_driver():
    """获取driver"""
    capabilities = {
        "platformName": "Android",
        # "automationName": "UiAutomator2",
        "deviceName": "ac05b72c",
        # "deviceName": "83e54a4c384e4a31",
        "app": "/Users/SongX/Downloads/boboshu.apk",
        # "appWaitActivity": "com.eduu.bang.app.SplashActivity",  # 需要等待切换activity(真机常见问题)
        "noReset": "true",  # 不用每次启动都重置应用
        "unicodeKeyboard": "true",  # 使用unicode编码方式发送字符串
        "resetKeyboard": "true"  # 是否重置键盘
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    return driver


def b():
    return "商城"
    # return 'new UiSelector().text("我的")'


def a():
    c = 'new UiSelector().text(' + '\"' + b() + '\"' + ')'
    # driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    driver.find_element_by_android_uiautomator(c).click()


driver = get_driver()
time.sleep(8)
a()
