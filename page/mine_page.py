from log import user_log
from util.get_by_local import GetByLocal

logger = user_log.logger


class MinePage:
    """获取我的模块所有的页面元素信息"""

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def aaa(self, element):
        if element == None:
            logger.error("section or option not right. Please check it.")
        else:
            try:
                element
            except Exception as e:
                logger.error(e)
        return element

    def get_mine_tab_element(self):
        """获取我的tab元素信息"""
        element = self.get_by_local.get_element('mine_element1', 'mine_tab')
        return self.aaa(element)

    def get_user_image_element(self):
        """获取头像元素信息"""
        return self.get_by_local.get_element('mine_element', 'user_image')

    def get_user_name_element(self):
        """获取用户名元素信息"""
        return self.get_by_local.get_element('mine_element', 'user_name')

    def get_login_title_element(self):
        """获取登录标题元素信息"""
        return self.get_by_local.get_element('mine_element', 'login_title')

    def get_friend_button_element(self):
        """获取好友元素信息"""
        return self.get_by_local.get_element('mine_element', 'friend_button')

    def get_collect_button_element(self):
        """获取收藏元素信息"""
        return self.get_by_local.get_element('mine_element', 'collect_button')

    def get_notice_button_element(self):
        """获取消息元素信息"""
        return self.get_by_local.get_element('mine_element', 'notice_button')

    def get_sign_button_element(self):
        """获取签到元素信息"""
        return self.get_by_local.get_element('mine_element', 'sign_button')

    def get_onePrice_button_element(self):
        """获取一元购课元素信息"""
        return self.get_by_local.get_element('mine_element', 'onePrice_button')

    def get_myCourse_button_element(self):
        """获取我的课程元素信息"""
        return self.get_by_local.get_element('mine_element', 'myCourse_button')

    def get_inviteReward_button_element(self):
        """获取邀请奖励元素信息"""
        return self.get_by_local.get_element('mine_element', 'inviteReward_button')

    def get_welfare_button_element(self):
        """获取福利中心元素信息"""
        return self.get_by_local.get_element('mine_element', 'welfare_button')

    def get_ad_button_element(self):
        """获取广告元素信息"""
        return self.get_by_local.get_element('mine_element', 'ad_button')

    def get_childInfo_button_element(self):
        """获取孩子档案元素信息"""
        return self.get_by_local.get_element('mine_element', 'childInfo_button')

    def get_childInfoIntroduce_element(self):
        """获取孩子档案介绍元素信息"""
        return self.get_by_local.get_element('mine_element', 'childInfoIntroduce')

    def get_showcaseView_button_element(self):
        """获取我的发表元素信息"""
        return self.get_by_local.get_element('mine_element', 'showcaseView_button')

    def get_courseOrder_button_element(self):
        """获取课程订单元素信息"""
        return self.get_by_local.get_element('mine_element', 'courseOrder_button')

    def get_orderIntroduce_element(self):
        """获取课程订单介绍元素信息"""
        return self.get_by_local.get_element('mine_element', 'orderIntroduce')

    def get_growthRecord_button_element(self):
        """获取成长记录元素信息"""
        return self.get_by_local.get_element('mine_element', 'growthRecord_button')

    def get_growthRecordNewFlag_element(self):
        """获取成长记录NEW元素信息"""
        return self.get_by_local.get_element('mine_element', 'growthRecordNewFlag')

    def get_growthRecordIntroduce_element(self):
        """获取成长记录介绍元素信息"""
        return self.get_by_local.get_element('mine_element', 'growthRecordIntroduce')

    def get_browseHistory_button_element(self):
        """获取浏览记录元素信息"""
        return self.get_by_local.get_element('mine_element', 'browseHistory_button')

    def get_historyPush_button_element(self):
        """获取历史推送元素信息"""
        return self.get_by_local.get_element('mine_element', 'historyPush_button')

    def get_historyPushIntroduce_element(self):
        """获取历史推送介绍元素信息"""
        return self.get_by_local.get_element('mine_element', 'historyPushIntroduce')

    def get_help_feedback_button_element(self):
        """获取帮助与反馈元素信息"""
        return self.get_by_local.get_element('mine_element', 'help_feedback_button')

    def get_setting_button_element(self):
        """获取设置元素信息"""
        return self.get_by_local.get_element('mine_element', 'setting_button')


if __name__ == '__main__':
    m = MinePage(driver=1)
    m.aaa('mine_element1', 'mine_tab')
