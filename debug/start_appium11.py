import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal
from page.mine_page import MinePage


def get_driver():
    """获取driver"""
    capabilities = {
        "platformName": "Android",
        # "automationName": "UiAutomator2",
        # "deviceName": "192.168.56.101:5555",
        # "deviceName": "83e54a4c384e4a31",
        "deviceName": "ac05b72c",
        "app": "/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/data/JZB_7.0.8-website-release.apk",
        # "appWaitActivity": "com.eduu.bang.app.SplashActivity",  # 需要等待切换activity(真机常见问题)
        "noReset": "true",  # 不用每次启动都重置应用
        "unicodeKeyboard": "true",  # 使用unicode编码方式发送字符串
        "resetKeyboard": "true"  # 是否重置键盘
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    return driver


def get_size():
    """获取屏幕宽和高"""
    size = driver.get_window_size()  # 返回字典{'height': 2560, 'width': 1440}
    height = size['height']  # y
    width = size['width']  # x
    print(size)
    # return width, height  # 返回元祖(1440, 2560)


def swipe_left():
    """向左滑动"""
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


def swipe_right():
    """向右滑动"""
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)


def swipe_up():
    """向上滑动"""
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y)


def swipe_down():
    """向下滑动"""
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


def swipe_on(direction):
    """滑动封装"""
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


def countdown_time():
    """跳过启动引导页"""
    driver.find_element_by_id('com.eduu.bang:id/tv_countdown_time').click()
    driver.find_element_by_id('com.eduu.bang:id/etSearch')


def go_login():
    """进入我的页面"""
    driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    # login_page()


# 登录操作
def login_page():
    get_by_local = GetByLocal(driver)
    get_by_local.get_element('username1').send_keys('13439075603')
    get_by_local.get_element('password').send_keys('1qaz2wsx')
    get_by_local.get_element('login_button').click()


def login_by_uiautomator():
    """uiautomator定位"""
    driver.find_element_by_android_uiautomator('new UiSelector().text("用户名/邮箱/手机号")').send_keys('13439075603')
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.eduu.bang:id/etPassword")').send_keys(
        '1qaz2wsx')


def login_by_xpath():
    """xpath定位"""
    driver.find_element_by_xpath("//android.widget.TextView[@text='手机号注册']").click()
    driver.find_element_by_xpath("//*[@class='android.widget.TextView'][0]").click()
    driver.find_element_by_xpath("//*[@class='android.widget.TextView' and @index='1']").click()


# 帮助与反馈页面
def go_webview():
    driver.find_element_by_android_uiautomator('new UiSelector().text("帮助与反馈")').click()


def get_webview():
    """切换到webview"""
    go_webview()
    webviews = driver.contexts
    for viw in webviews:
        if 'WEBVIEW_com.eduu.bang' in viw:
            driver.switch_to.context(viw)
            break
    # print(webviews)
    try:
        driver.find_element_by_id('com.eduu.bang:id/appBackDir').click()
    except Exception as e:
        driver.switch_to.context(webviews[0])
        driver.find_element_by_id('com.eduu.bang:id/appBackDir').click()
        raise e


# toast获取
def get_toast():
    driver.find_element_by_id('com.eduu.bang:id/btnEduuLogin').click()  # 不输入内容点击登录按钮
    driver.find_element_by_class_name()
    toast_element = ("xpath", "//*[contains(@text,'信息不能为空')]")
    # 找10秒钟，每0.1秒找一次，找到元素为止
    print('toast元素为：', WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_element)))


driver = get_driver()  # 全局
# countdown_time()
time.sleep(6)
m = MinePage(driver)
m.get_mine_tab_element().click()
m.get_user_image_element().click()

time.sleep(3)
driver.quit()
