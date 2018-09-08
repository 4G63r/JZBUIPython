from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class SearchPage:
    """获取搜索模块所有的页面元素信息"""

    def __init__(self, i):
        base_driver = BaseDriver()
        driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(driver)

    def get_headline_search_element(self):
        """获取头条搜索框元素信息"""
        return self.get_by_local.get_element('headline_element', 'search_input')

    def get_parent_university_search_element(self):
        """获取家长大学搜索框元素信息"""
        return self.get_by_local.get_element('parent_university_element', 'search_input')

    def get_community_search_element(self):
        """获取社区搜索框元素信息"""
        return self.get_by_local.get_element('community_element', 'search_input')

    def get_allBang_search_element(self):
        """获取社区搜索框元素信息"""
        return self.get_by_local.get_element('community_element', 'search_input_bang')

    def get_search_input_element(self):
        """获取搜索输入框元素信息"""
        return self.get_by_local.get_element('search_element', 'search_input')

    def get_search_input_clear_element(self):
        """获取搜索输入框清除按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'search_input_clear')

    def get_back_element(self):
        """获取返回按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'back')

    def get_search_button_element(self):
        """获取搜索按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'search_button')

    def get_tab_elements(self):
        """获取内容/课程/用户标签元素信息"""
        return self.get_by_local.get_element('search_element', 'tab')

    def get_title_elements(self):
        """
        获取热门搜索/搜索历史/
        学校/帖子/帖子list标题/帮/热门头条/热门头条list标题元素信息
        """
        return self.get_by_local.get_element('search_element', 'title')

    def get_preset_search_elements(self):
        """获取默认搜索词/搜索历史元素信息"""
        return self.get_by_local.get_element('search_element', 'preset_search')

    def get_clear_all_history_element(self):
        """获取删除全部历史按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'clear_all_history')

    def get_clear_one_history_elements(self):
        """获取单个历史删除按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'clear_one_history')

    def get_clear_window_title_element(self):
        """获取删除弹框标题元素信息"""
        return self.get_by_local.get_element('search_element', 'clear_window_title')

    def get_cancel_button_element(self):
        """获取删除弹框取消按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'cancel_button')

    def get_clear_button_element(self):
        """获取删除弹框清除按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'clear_button')

    def get_more_elements(self):
        """获取更多按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'more_button')

    def get_school_list_elements(self):
        """获取学校/帮列表标题元素信息"""
        return self.get_by_local.get_element('search_element', 'school_bang_list_title')

    def get_school_follow_button_elements(self):
        """获取学校关注按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'school_follow_button')

    def get_bang_follow_button_elements(self):
        """获取帮关注按钮元素信息"""
        return self.get_by_local.get_element('search_element', 'bang_follow_button')

    def get_post_list_summary_elements(self):
        """获取帖子摘要/帮关注数元素信息"""
        return self.get_by_local.get_element('search_element', 'post_list_summary')

    def get_post_list_time_elements(self):
        """获取帖子列表时间元素信息"""
        return self.get_by_local.get_element('search_element', 'post_list_time')

    def get_post_list_comment_elements(self):
        """获取帖子列表评论数元素信息"""
        return self.get_by_local.get_element('search_element', 'post_list_comment_count')

    # def get_content_tab_element(self):
    #     """获取内容标签元素信息"""
    #     return self.get_by_local.get_element('search_element', 'content_tab')
    #
    # def get_course_tab_element(self):
    #     """获取课程标签元素信息"""
    #     return self.get_by_local.get_element('search_element', 'course_tab')
    #
    # def get_user_tab_element(self):
    #     """获取用户标签元素信息"""
    #     return self.get_by_local.get_element('search_element', 'user_tab')
    #
    # def get_hot_search_element(self):
    #     """获取热门搜索元素信息"""
    #     return self.get_by_local.get_element('search_element', 'hot_search')
    #
    # def get_search_history_element(self):
    #     """获取搜索历史元素信息"""
    #     return self.get_by_local.get_element('search_element', 'search_history')
    #
    # def get_bang_title_element(self):
    #     """获取帮元素信息"""
    #     return self.get_by_local.get_element('search_element', 'bang_title')
    #
    # def get_hot_headline_title_element(self):
    #     """获取热门头条元素信息"""
    #     return self.get_by_local.get_element('search_element', 'title_hot_headline')
    #
    # def get_post_title_element(self):
    #     """获取帖子标题元素信息"""
    #     return self.get_by_local.get_element('search_element', 'post_title')
    #
    # def get_post_list_title_element(self):
    #     """获取帖子列表标题元素信息"""
    #     return self.get_by_local.get_element('search_element', 'post_list_title')
    #
    # def get_school_title_element(self):
    #     """获取学校标题元素信息"""
    #     return self.get_by_local.get_element('search_element', 'school_title')
