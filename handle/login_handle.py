from page.login_page import LoginPage


class LoginHandle:
    """操作登录页面的元素"""

    def __init__(self):
        self.login_page = LoginPage()

    def send_username(self, user):
        # 输入用户名
        self.login_page.get_username_element().send_keys(user)

    def send_passwd(self, passwd):
        # 输入密码
        self.login_page.get_passwd_element().send_keys(passwd)

    def click_login_button(self):
        # 点击登录按钮
        self.login_page.get_login_button_element().click()

    def click_register(self):
        # 点击注册按钮
        self.login_page.get_register_element().click()

    def click_forget_passwd(self):
        # 点击找回密码按钮
        self.login_page.get_forget_passwd_element().click()

    def click_login_by_qq(self):
        # 点击QQ登录按钮
        self.login_page.get_login_by_qq_element().click()

    def click_login_by_wx(self):
        # 点击微信登录按钮
        self.login_page.get_login_by_wx_element().click()

    def click_login_by_sina(self):
        # 点击新浪微博登录按钮
        self.login_page.get_login_by_sina_element().click()

    def click_skip(self):
        # 点击跳过按钮
        self.login_page.get_skip_element().click()

    def click_back(self):
        # 点击左上角返回按钮
        self.login_page.get_back_element().click()

    def get_fail_toast(self, message):
        # 获取toast，根据返回信息进行反数据,信息不能为空  用户名或密码验证失败  密码至少6位
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
