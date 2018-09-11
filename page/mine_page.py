from log import user_log
from util.get_by_local import GetByLocal

logger = user_log.logger


class MinePage:
    """获取我的模块所有的页面元素信息"""

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_mine_tab_element(self):
        """获取我的tab元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'mine_tab')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_user_image_element(self):
        """获取头像元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'user_image')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_user_name_element(self):
        """获取用户名元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'user_name')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_login_title_element(self):
        """获取登录标题元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'login_title')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_friend_button_element(self):
        """获取好友元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'friend_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_collect_button_element(self):
        """获取收藏元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'collect_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_notice_button_element(self):
        """获取消息元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'notice_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_sign_button_element(self):
        """获取签到元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'sign_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_onePrice_button_element(self):
        """获取一元购课元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'onePrice_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_myCourse_button_element(self):
        """获取我的课程元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'myCourse_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_inviteReward_button_element(self):
        """获取邀请奖励元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'inviteReward_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_welfare_button_element(self):
        """获取福利中心元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'welfare_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_ad_button_element(self):
        """获取广告元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'ad_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_childInfo_button_element(self):
        """获取孩子档案元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'childInfo_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_childInfoIntroduce_element(self):
        """获取孩子档案介绍元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'childInfoIntroduce')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_showcaseView_button_element(self):
        """获取我的发表元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'showcaseView_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_courseOrder_button_element(self):
        """获取课程订单元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'courseOrder_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_orderIntroduce_element(self):
        """获取课程订单介绍元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'orderIntroduce')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_growthRecord_button_element(self):
        """获取成长记录元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'growthRecord_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_growthRecordNewFlag_element(self):
        """获取成长记录NEW元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'growthRecordNewFlag')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_growthRecordIntroduce_element(self):
        """获取成长记录介绍元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'growthRecordIntroduce')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_browseHistory_button_element(self):
        """获取浏览记录元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'browseHistory_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_historyPush_button_element(self):
        """获取历史推送元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'historyPush_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_historyPushIntroduce_element(self):
        """获取历史推送介绍元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'historyPushIntroduce')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_help_feedback_button_element(self):
        """获取帮助与反馈元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'help_feedback_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element

    def get_setting_button_element(self):
        """获取设置元素信息"""
        global element
        try:
            element = self.get_by_local.get_element('mine_element', 'setting_button')
            if element == None:
                logger.error("section or option not right. Please check it.")
        except Exception as e:
            logger.error(e)
        return element
