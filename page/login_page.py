import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal


class LoginPage:
    """获取登录页所有的页面元素信息"""

    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver()
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        # 获取用户名元素信息
        return self.get_by_local.get_element('username')

    def get_passwd_element(self):
        # 获取密码元素信息
        return self.get_by_local.get_element('passwd')

    def get_login_button_element(self):
        # 获取登录按钮元素信息
        return self.get_by_local.get_element('login_button')

    def get_register_element(self):
        # 获取手机号注册元素信息
        return self.get_by_local.get_element('register')

    def get_forget_passwd_element(self):
        # 获取找回密码元素信息
        return self.get_by_local.get_element('forget_passwd')

    def get_login_by_qq_element(self):
        # 获取QQ登录按钮元素信息
        return self.get_by_local.get_element('login_by_qq')

    def get_login_by_wx_element(self):
        # 获取微信登录按钮元素信息
        return self.get_by_local.get_element('login_by_wx')

    def get_login_by_sina_element(self):
        # 获取新浪微博登录按钮元素信息
        return self.get_by_local.get_element('login_by_sina')

    def get_skip_element(self):
        # 获取跳过按钮元素信息
        return self.get_by_local.get_element('skip')

    def get_back_element(self):
        # 获取返回按钮元素信息
        return self.get_by_local.get_element('back')

    def get_toast_element(self, message):
        # 获取toast元素信息
        time.sleep(3)
        toast_element = ("xpath", "//*[contains(@text," + message + ")]")
        # 找10秒钟，每0.1秒找一次，找到元素为止
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
