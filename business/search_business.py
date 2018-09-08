from handle.search_handle import SearchHandle


class SearchBusiness:
    def __init__(self, i):
        self.search_handle = SearchHandle(i)

    def go_search(self, page):
        """从哪个页面进入搜索"""
        if page == '头条':
            self.search_handle.click_headline_search_element()
        elif page == '家长大学':
            self.search_handle.click_parent_university_search_element()
        elif page == '社区':
            self.search_handle.click_community_search_element()
        else:
            pass

    def go_search_pass(self):
        """
        成功进入搜索页面
        判断条件是或者3个tab和热门搜索标题
        """
        flag1 = False
        flag2 = False
        tabs = ['内容', '课程', '用户1']
        titles = ['热门搜索', '搜索历史']
        self.go_search('头条')
        if tabs == self.search_handle.get_tab_texts():
            flag1 = True
        for i in self.search_handle.get_hot_history_texts():
            if i in titles:
                flag2 = True
        if flag1 == flag2:
            return True

    def search_pass_preset(self):
        """默认搜索词发起搜索通过"""

    def search_pass(self):
        """搜索通过"""
        flag = False
        self.search_handle.send_search_keyword('小')
        self.search_handle.click_search_button()
        for i in self.search_handle.get_school_list_titles():
            if '小' in i:
                flag = True
            else:
                print("搜索结果不正确")

    def back(self):
        self.search_handle.click_back_button()


if __name__ == '__main__':
    search_business = SearchBusiness(0)
    search_business.search_pass()
