from page.mine_page import MinePage


class MineHandle:
    """操作我的页面的元素"""

    def __init__(self, driver):
        self.mine_page = MinePage(driver)

    def click_mine_tab_element(self):
        """点击我的tab元素"""
        self.mine_page.get_mine_tab_element()[0].click()

    def click_user_image_element(self):
        """点击头像元素"""
        self.mine_page.get_user_image_element()[0].click()

    def get_user_name(self):
        """获取用户名"""
        return self.mine_page.get_user_name_element()[0].text

    def get_login_title(self):
        """获取登录文案"""
        return self.mine_page.get_login_title_element()[0].text

    def click_friend_button_element(self):
        """点击好友元素"""
        self.mine_page.get_friend_button_element()[0].click()

    def click_collect_button_element(self):
        """点击收藏元素"""
        self.mine_page.get_collect_button_element()[0].click()

    def click_notice_button_element(self):
        """点击消息元素"""
        self.mine_page.get_notice_button_element()[0].click()

    def click_sign_button_element(self):
        """点击签到元素"""
        self.mine_page.get_sign_button_element()[0].click()

    def click_onePrice_button_element(self):
        """点击一元购课元素"""
        self.mine_page.get_onePrice_button_element()[0].click()

    def click_myCourse_button_element(self):
        """点击我的课程元素"""
        self.mine_page.get_myCourse_button_element()[0].click()

    def click_inviteReward_button_element(self):
        """点击邀请奖励元素"""
        self.mine_page.get_inviteReward_button_element()[0].click()

    def click_welfare_button_element(self):
        """点击福利中心元素"""
        self.mine_page.get_welfare_button_element()[0].click()

    def click_ad_button_element(self):
        """点击广告元素"""
        self.mine_page.get_ad_button_element()[0].click()

    def click_childInfo_button_element(self):
        """点击孩子档案元素"""
        self.mine_page.get_childInfo_button_element()[0].click()

    def get_childInfoIntroduce(self):
        """获取孩子档案"""
        return self.mine_page.get_childInfoIntroduce_element()[0].text

    def click_showcaseView_button_element(self):
        """点击我的发表元素"""
        self.mine_page.get_showcaseView_button_element()[0].click()

    def click_courseOrder_button_element(self):
        """点击课程订单元素"""
        self.mine_page.get_courseOrder_button_element()[0].click()

    def get_orderIntroduce(self):
        """获取课程订单介绍"""
        return self.mine_page.get_orderIntroduce_element()[0].text

    def click_growthRecord_button_element(self):
        """点击成长记录元素"""
        self.mine_page.get_growthRecord_button_element()[0].click()

    def get_growthRecordNewFlag(self):
        """获取成长记录NEW"""
        return self.mine_page.get_growthRecordNewFlag_element()[0].text

    def get_growthRecordIntroduce(self):
        """获取成长记录介绍"""
        return self.mine_page.get_growthRecordIntroduce_element()[0].text

    def click_browseHistory_button_element(self):
        """点击浏览记录元素"""
        self.mine_page.get_browseHistory_button_element()[0].click()

    def click_historyPush_button_element(self):
        """点击历史推送元素"""
        self.mine_page.get_historyPush_button_element()[0].click()

    def get_historyPushIntroduce(self):
        """获取历史推送介绍"""
        return self.mine_page.get_historyPushIntroduce_element()[0].text

    def click_help_feedback_button_element(self):
        """点击帮助与反馈元素"""
        self.mine_page.get_help_feedback_button_element()[0].click()

    def click_setting_button_element(self):
        """点击账号与设置元素"""
        self.mine_page.get_setting_button_element()[0].click()
