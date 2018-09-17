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

    def go_mine(self):
        """成功进入我的页面&验证"""
        self.mh.click_mine_tab_element()
        if self.check_user_isTourist():
            if self.mh.get_login_title() == '登录' and self.ea.element_exist(
                    self.mp.get_user_image_element()) and self.ea.element_exist(
                self.mp.get_sign_btn_element()):
                return True
            else:
                return False
        else:
            try:
                self.mp.get_login_title_element() == '登录'
                self.mh.get_collect_count() == '1'
                return False
            except:
                self.mh.get_collect_count() == '1'
                return True

    def user_image(self):
        """我的页面头像点击跳转"""
        if self.check_user_isTourist():
            self.mh.click_user_image_element()
            if self.lh.get_login_title() == "手机号登录" and self.ea.element_exist(
                    self.lp.get_qq_btn_element()) and self.ea.element_exist(
                self.lp.get_weibo_btn_element()) and self.ea.element_exist(self.lp.get_loginPage_wechat_element()):
                return True
            else:
                return False
        else:
            user_name = self.mh.get_user_name()
            self.mh.click_user_image_element()
            if self.ea.get_text(self.mp.get_userName_element()) == user_name and self.ea.element_exist(
                    self.mp.get_updatePersonal_element()) and len(
                self.ea.get_text(self.mp.get_threadName_element())) > 0:
                return True
            else:
                return False

    def friend(self):
        """我的页面好友按钮点击跳转"""
        if self.check_user_isTourist():
            self.mh.click_friend_btn_element()
            if self.ea.element_exist(self.lp.get_login_panel_element()) and self.ea.element_exist(
                    self.lp.get_register_btn_element()):
                return True
            else:
                return False
        else:
            self.mh.click_friend_btn_element()
            if self.ea.element_exist(self.mp.get_agency_element()) and self.ea.element_exist(
                    self.mp.get_friend_title_element()) and self.ea.element_exist(
                self.mp.get_recommend_friend_element()):
                return True
            else:
                return False

    def collect(self):
        """我的页面收藏按钮点击跳转"""
        if self.check_user_isTourist():
            self.mh.click_collect_btn_element()
            if self.ea.element_exist(self.lp.get_login_panel_element()) and self.ea.element_exist(
                    self.lp.get_register_btn_element()):
                return True
            else:
                return False
        else:
            self.mh.click_collect_btn_element()
            if self.ea.element_exist(self.mp.get_collect_time_element()) and self.ea.element_exist(
                    self.mp.get_collect_title_element()):
                return True
            else:
                return False

    def notice(self):
        """我的页面消息按钮点击跳转"""
        self.mh.click_notice_btn_element()
        if self.ea.element_exist(self.mp.get_notice_sendLetter_element()) and self.ea.element_exist(
                self.mp.get_notice_1_element()) and self.ea.element_exist(self.mp.get_notice_bang_element()):
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
        flag = False
        el_lists = [
            self.mp.get_friend_btn_element(), self.mp.get_collect_btn_element(),
            self.mp.get_sign_btn_element(), self.mp.get_childInfo_btn_element(),
            self.mp.get_showcaseView_btn_element(), self.mp.get_courseOrder_btn_element()
        ]
        if self.check_user_isTourist():
            for i in el_lists:
                self.ea.click(i)
                if self.ea.element_exist(self.lp.get_login_panel_element()):
                    flag = True
                    self.lh.click_close_btn()
                else:
                    flag = False
                    break
            return flag

    def growthRecord(self):
        """未登录测试点击成长记录是否有登录注册弹框"""
        self.ea.click(self.mp.get_growthRecord_btn_element())
        if self.ea.element_exist(self.lp.get_login_panel_element()):
            self.lh.click_close_btn()
            return True
        else:
            return False

    def aa(self):
        self.mh.click_user_image_element()
