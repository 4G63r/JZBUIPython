from util.get_by_local import GetByLocal
from util.read_ini import ReadIni


class LoginPage:
    """获取登录页所有的页面元素信息"""

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        self.read_ini = ReadIni()

    def wait_element(self, section, option):
        """元素等待&获取元素信息"""
        value = self.read_ini.get_value(section, option)
        self.get_by_local.element_wait(section, option)
        el = self.get_by_local.get_element(section, option)
        return value, el

    def get_login_panel_element(self):
        """获取登录/注册弹框元素信息"""
        return self.wait_element('login_panel_element', 'login_panel')

    def get_close_btn_element(self):
        """获取关闭按钮元素信息"""
        return self.wait_element('login_panel_element', 'close_btn')

    def get_gift_image_element(self):
        """获取新人礼包图片元素信息"""
        return self.wait_element('login_panel_element', 'gift_image')

    def get_register_btn_element(self):
        """获取注册按钮元素信息"""
        return self.wait_element('login_panel_element', 'register_btn')

    def get_loginPanel_wechat_element(self):
        """获取弹框上微信登录元素信息"""
        return self.wait_element('login_panel_element', 'wechat_btn')

    def get_phone_btn_element(self):
        """获取手机登录元素信息"""
        return self.wait_element('login_panel_element', 'phone_btn')

    # ----------------------------------------------------------------------

    def get_loginPage_back_element(self):
        """获取登录页面返回按钮元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'back')

    def get_loginRegister_title_element(self):
        """获取标题元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'title_text')

    def get_phone_input_element(self):
        """获取手机号输入框元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'phone_input')

    def get_clear_btn_element(self):
        """获取清空按钮元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'clear_btn')

    def get_sendMsgCode_btn_element(self):
        """获取发送验证码按钮元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'sendMsgCode_btn')

    def get_bottom_text_element(self):
        """获取底部文案元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'bottom_text')

    def get_protocol_btn_element(self):
        """获取用户协议入口元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'protocol_btn')

    def get_pwLogin_btn_element(self):
        """获取密码登录入口元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'pwLogin_btn')

    def get_qq_btn_element(self):
        """获取QQ登录按钮元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'qq_btn')

    def get_loginPage_wechat_element(self):
        """获取微信登录按钮元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'wechat_btn')

    def get_weibo_btn_element(self):
        """获取微博登录元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'weibo_btn')

    # ----------------------------------------------------------------------

    def get_msg_title_element(self):
        """获取输入验证码页面标题元素信息"""
        return self.wait_element('phoneLoginRegister_element', 'title_text')

    def get_sendTo_text_element(self):
        """获取验证码已发送至xxx文案元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'sendTo_text')

    def get_code_input_element(self):
        """获取验证码输入框元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'code_input')

    def get_login_btn_element(self):
        """获取登录按钮元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'login_btn')

    def get_reSend_text_element(self):
        """获取重发文案"""
        return self.wait_element('sendMsgCode_page_element', 'reSend_text')

    def get_sendMsgBack_element(self):
        """获取输入验证码页面返回按钮元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'back')

    def get_alert_text_element(self):
        """获取确认框文案元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'alert_text')

    def get_alert_ok_elemnt(self):
        """获取确认框确认按钮元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'alert_ok')

    def get_alert_cancel_element(self):
        """获取确认框取消按钮元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'alert_cancel')

    # ----------------------------------------------------------------------

    def get_pwLoginBack_element(self):
        """获取用户名密码页返回按钮元素信息"""
        return self.wait_element('sendMsgCode_page_element', 'back')

    def get_title_element(self):
        """获取用户名密码页标题文案元素信息"""
        return self.wait_element('pwLogin_element', 'title')

    def get_findpw_btn_element(self):
        """获取找回密码元素信息"""
        return self.wait_element('pwLogin_element', 'findpw_btn')

    def get_user_input_element(self):
        """获取用户名输入框元素信息"""
        return self.wait_element('pwLogin_element', 'user_input')

    def get_pw_input_element(self):
        """获取密码输入框元素信息"""
        return self.wait_element('pwLogin_element', 'pw_input')

    def get_pwLoginBtn_element(self):
        """获取登录按钮元素信息"""
        return self.wait_element('pwLogin_element', 'login_btn')

    def get_tryPhone_text_element(self):
        """获取底部文案元素信息"""
        return self.wait_element('pwLogin_element', 'tryPhone_text')

    def get_tryPhone_btn_element(self):
        """获取手机号登录入口元素信息"""
        return self.wait_element('pwLogin_element', 'tryPhone_btn')
