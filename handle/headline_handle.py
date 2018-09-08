from page.headline_page import HeadlinePage


class HeadlineHandle:
    """操作头条页面的元素"""

    def __init__(self, i):
        self.headline_page = HeadlinePage(i)

    def click_search_box(self):
        """点击搜索框"""
        return self.headline_page.get_search_input_element().click()


if __name__ == '__main__':
    h = HeadlineHandle(0)
    h.click_search_box()
