from handle.login_handle import LoginHandle


class LoginBusiness:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login_pass(self):
        self.login_handle.send_username('13439075603')
        self.login_handle.send_passwd('1qaz2wsx')
        self.login_handle.click_login_button()

    # 用户名错误
    def login_user_error(self):
        self.login_handle.send_username('13439075641')
        self.login_handle.send_passwd('1qaz2wsx')
        self.login_handle.click_login_button()
        user_flag = self.login_handle.get_fail_toast('用户名或密码验证失败')
        if user_flag:
            return True
        else:
            return False

    # 密码错误
    def login_passwd_error(self):
        self.login_handle.send_username('13439075603')
        self.login_handle.send_passwd('1qaz2ws')
        self.login_handle.click_login_button()
        user_flag = self.login_handle.get_fail_toast('用户名或密码验证失败')
        if user_flag:
            return True
        else:
            return False

    # 密码错误
    def login_passwd_short(self):
        self.login_handle.send_username('13439075603')
        self.login_handle.send_passwd('1qaz2ws')
        self.login_handle.click_login_button()
        user_flag = self.login_handle.get_fail_toast('密码至少6位')
        if user_flag:
            return True
        else:
            return False

    # 不输入信息
    def login_none(self):
        self.login_handle.send_username('')
        self.login_handle.send_passwd('')
        self.login_handle.click_login_button()
        user_flag = self.login_handle.get_fail_toast('信息不能为空')
        if user_flag:
            return True
        else:
            return False
