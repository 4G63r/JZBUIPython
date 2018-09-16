from util.element_action import ElementAction
from page.mine_page import MinePage
from handle.mine_handle import MineHandle
from page.login_page import LoginPage
from handle.login_handle import LoginHandle
from log.print_log import Log

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "


class MineBusiness:
    """我的模块业务交互"""

    def __init__(self, driver):
        self.mp = MinePage(driver)
        self.mh = MineHandle(driver)
        self.lp = LoginPage(driver)
        self.lh = LoginHandle(driver)
        self.ea = ElementAction(driver)

    def check_user_isTourist(self):
        """检查用户身份"""
        if self.mh.get_user_name() == '游客':
            return True
        else:
            return False

    def go_mine_pass(self):
        """成功进入我的页面&验证"""
        self.mh.click_mine_tab_element()
        if self.ea.element_exist(self.mp.get_user_image_element()) and self.ea.element_exist(
                self.mp.get_sign_btn_element()):
            return True
        else:
            return False

    def login_pass(self):
        """成功登录
        1、以游客判断登录状态，如果是游客身份
        2、点击我的头像，进入手机号登录页面
        3、输入手机号，点击发送验证码
        4、输入验证码页面输入验证码点击登录
        5、再次以是否为游客判断是否登录成功
        """
        if self.mh.get_user_name == '游客':
            self.mh.click_user_image_element()

    def test_loginRegister_panel(self):
        """测试未登录时的登录注册弹框"""
        self.ea.swipe_on('up')
        flag = False
        el_lists = [
            self.mp.get_friend_btn_element(), self.mp.get_collect_btn_element(),
            self.mp.get_sign_btn_element(), self.mp.get_childInfo_btn_element(),
            self.mp.get_showcaseView_btn_element(), self.mp.get_courseOrder_btn_element()
        ]
        if self.check_user_isTourist():
            for i in el_lists:
                self.ea.click(i)
                if self.ea.element_exist(self.lp.get_login_panel_element()) == True:
                    flag = True
                    self.lh.click_close_btn()
                else:
                    flag = False
                    break
            return flag

    def aa(self):
        self.mh.click_user_image_element()
