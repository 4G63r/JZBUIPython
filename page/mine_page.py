import time

from util.get_by_local import GetByLocal
from util.read_ini import ReadIni
from log.print_log import Log

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "


class MinePage:
    """获取我的模块所有的页面元素信息"""

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        self.read_ini = ReadIni()

    def wait_element(self, section, option):
        """元素等待&获取元素信息"""
        global value
        start_t = time.time()
        try:
            value = self.read_ini.get_value(section, option)
            self.get_by_local.element_wait(section, option)
            el = self.get_by_local.get_element(section, option)
            logger.info(
                "{0} Get element: <{1}>, Spend {2} seconds".format(success, value, round(time.time() - start_t, 2)))
            return value, el
        except Exception:
            logger.info(
                "{0} Unable to get element <{1}>, Spend {2} seconds".format(fail, value,
                                                                            round(time.time() - start_t, 2)))
            raise

    def get_mine_tab_element(self):
        """获取我的tab元素信息"""
        return self.wait_element('mine_element', 'mine_tab')

    def get_user_image_element(self):
        """获取头像元素信息"""
        return self.wait_element('mine_element', 'user_image')

    def get_user_name_element(self):
        """获取用户名元素信息"""
        return self.wait_element('mine_element', 'user_name')

    def get_login_title_element(self):
        """获取登录标题元素信息"""
        return self.wait_element('mine_element', 'login_title')

    def get_friend_btn_element(self):
        """获取好友元素信息"""
        return self.wait_element('mine_element', 'friend_btn')

    def get_collect_btn_element(self):
        """获取收藏元素信息"""
        return self.wait_element('mine_element', 'collect_btn')

    def get_notice_btn_element(self):
        """获取消息元素信息"""
        return self.wait_element('mine_element', 'notice_btn')

    def get_sign_btn_element(self):
        """获取签到元素信息"""
        return self.wait_element('mine_element', 'sign_btn')

    def get_onePrice_btn_element(self):
        """获取一元购课元素信息"""
        return self.wait_element('mine_element', 'onePrice_btn')

    def get_myCourse_btn_element(self):
        """获取我的课程元素信息"""
        return self.wait_element('mine_element', 'myCourse_btn')

    def get_inviteReward_btn_element(self):
        """获取邀请奖励元素信息"""
        return self.wait_element('mine_element', 'inviteReward_btn')

    def get_welfare_btn_element(self):
        """获取福利中心元素信息"""
        return self.wait_element('mine_element', 'welfare_btn')

    def get_ad_btn_element(self):
        """获取广告元素信息"""
        return self.wait_element('mine_element', 'ad_btn')

    def get_childInfo_btn_element(self):
        """获取孩子档案元素信息"""
        return self.wait_element('mine_element', 'childInfo_btn')

    def get_childInfoIntroduce_element(self):
        """获取孩子档案介绍元素信息"""
        return self.wait_element('mine_element', 'childInfoIntroduce')

    def get_showcaseView_btn_element(self):
        """获取我的发表元素信息"""
        return self.wait_element('mine_element', 'showcaseView_btn')

    def get_courseOrder_btn_element(self):
        """获取课程订单元素信息"""
        return self.wait_element('mine_element', 'courseOrder_btn')

    def get_orderIntroduce_element(self):
        """获取课程订单介绍元素信息"""
        return self.wait_element('mine_element', 'orderIntroduce')

    def get_growthRecord_btn_element(self):
        """获取成长记录元素信息"""
        return self.wait_element('mine_element', 'growthRecord_btn')

    def get_growthRecordNewFlag_element(self):
        """获取成长记录NEW元素信息"""
        return self.wait_element('mine_element', 'growthRecordNewFlag')

    def get_growthRecordIntroduce_element(self):
        """获取成长记录介绍元素信息"""
        return self.wait_element('mine_element', 'growthRecordIntroduce')

    def get_browseHistory_btn_element(self):
        """获取浏览记录元素信息"""
        return self.wait_element('mine_element', 'browseHistory_btn')

    def get_historyPush_btn_element(self):
        """获取历史推送元素信息"""
        return self.wait_element('mine_element', 'historyPush_btn')

    def get_historyPushIntroduce_element(self):
        """获取历史推送介绍元素信息"""
        return self.wait_element('mine_element', 'historyPushIntroduce')

    def get_help_feedback_btn_element(self):
        """获取帮助与反馈元素信息"""
        return self.wait_element('mine_element', 'help_feedback_btn')

    def get_setting_btn_element(self):
        """获取设置元素信息"""
        return self.wait_element('mine_element', 'setting_btn')
