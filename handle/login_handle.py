from page.login_page import LoginPage
from util.element_action import ElementAction


class LoginHandle:
    """操作登录页面的元素"""

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.ea = ElementAction(driver)

    def click_close_btn(self):
        """点击登录注册弹框上面的关闭按钮"""
        self.ea.click(self.login_page.get_close_btn_element())

    def input_phone(self):
        """输入手机号"""
        self.ea.clear_input(self.login_page.get_phone_input_element(), '13439075603')

    def get_login_title(self):
        """获取登录页面标题文案"""
        return self.ea.get_text(self.login_page.get_loginRegister_title_element())

    def click_sendMsgCode_btn(self):
        """点击发送验证码按钮"""
        self.ea.click(self.login_page.get_sendMsgCode_btn_element())

    def get_msg_title(self):
        """获取输入验证码页面标题文案"""
        return self.ea.get_text(self.login_page.get_msg_title_element())

    def input_msgCode(self):
        """输入验证码"""
        self.ea.clear_input(self.login_page.get_code_input_element(), '4456')

    def click_login_btn(self):
        """点击登录按钮"""
        self.ea.click(self.login_page.get_login_btn_element())

    def click_back_btn(self):
        """点击返回按钮"""
        self.ea.click(self.login_page.get_loginPage_back_element())
