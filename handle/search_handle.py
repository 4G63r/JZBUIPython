from page.search_page import SearchPage


class SearchHandle:
    """操作搜索页面的元素"""

    def __init__(self, i):
        self.search_page = SearchPage(i)

    def click_headline_search_element(self):
        """点击头条搜索框"""
        self.search_page.get_headline_search_element().click()

    def click_parent_university_search_element(self):
        """点击家长大学搜索框"""
        self.search_page.get_parent_university_search_element().click()

    def click_community_search_element(self):
        """点击社区搜索框"""
        self.search_page.get_community_search_element().click()

    def send_search_keyword(self, keyword):
        """输入搜索词"""
        self.search_page.get_search_input_element().send_keys(keyword)

    def get_preset_input_text(self):
        """获取搜索框默认搜索词"""
        return self.search_page.get_search_input_element().text

    def click_search_clear_button(self):
        """点击搜索框清除按钮"""
        self.search_page.get_search_input_clear_element().click()

    def click_search_button(self):
        """点击搜索按钮"""
        self.search_page.get_search_button_element().click()

    def click_back_button(self):
        """点击返回按钮"""
        self.search_page.get_back_element().click()

    def get_tab_texts(self):
        """获取标签文案"""
        list = []
        elements = self.search_page.get_tab_elements()
        for i in elements:
            list.append(i.text)
        return list

    def click_content_tab(self):
        """点击内容标签"""
        elements = self.search_page.get_tab_elements()
        elements[0].click()

    def click_course_tab(self):
        """点击课程标签"""
        elements = self.search_page.get_tab_elements()
        elements[1].click()

    def click_user_tab(self):
        """点击用户标签"""
        elements = self.search_page.get_tab_elements()
        elements[2].click()

    def get_hot_history_texts(self):
        """获取热门搜索和搜索历史文案"""
        list = []
        elements = self.search_page.get_title_elements()
        for i in elements:
            list.append(i.text)
        return list

    # def get_hot_search_text(self):
    #     """获取热门搜索文案"""
    #     return self.search_page.get_hot_search_element().text

    def click_preset_search(self):
        """点击默认搜索词"""
        self.search_page.get_preset_search_element().click()

    # def get_search_history_text(self):
    #     """获取搜索历史文案"""
    #     return self.search_page.get_search_history_element().text

    def click_clear_history_button(self):
        """点击搜索历史清除按钮"""
        self.search_page.get_clear_all_history_element().click()

    def clear_one_history(self):
        """删除单个历史"""
        self.search_page.get_clear_one_history_element().click()

    def get_clear_window_text(self):
        """获取清除弹框文案"""
        return self.search_page.get_clear_window_title_element().text

    def click_cancel_button(self):
        """点击取消按钮"""
        self.search_page.get_cancel_button_element().click()

    def click_clear_button(self):
        """点击清除按钮"""
        self.search_page.get_clear_button_element().click()

    def get_school_text(self):
        """获取学校标题文案"""
        return self.search_page.get_school_title_element().text

    def click_more_button(self):
        """点击更多按钮"""
        self.search_page.get_more_elements().click()

    def get_school_list_titles(self):
        """获取学校列表标题文案"""
        list = []
        elements = self.search_page.get_school_list_elements()
        for i in elements:
            list.append(i.text)
        return list

    def click_follow_button(self):
        """点击关注按钮"""
        self.search_page.get_follow_button_element().click()

    def get_post_text(self):
        """获取帖子标题文案"""
        return self.search_page.get_post_title_element().text

    def get_post_list_text(self):
        """获取帖子列表标题文案"""
        return self.search_page.get_post_list_title_element().text

    def get_post_list_summary(self):
        """获取帖子列表摘要文案"""
        return self.search_page.get_post_list_summary_element().text

    def get_post_list_time(self):
        """获取帖子列表时间"""
        return self.search_page.get_post_list_time_element().text

    def get_post_list_comment(self):
        """获取帖子列表评论数"""
        return self.search_page.get_post_list_comment_element().text

    def get_bang_text(self):
        """获取帮标题文案"""
        return self.search_page.get_bang_title_element().text

    def get_hot_headline_text(self):
        """获取热门头条标题文案"""
        return self.search_page.get_hot_headline_title_element().text
