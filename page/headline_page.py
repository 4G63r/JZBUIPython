from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal


class HeadlinePage:
    """获取头条tab所有的页面元素信息"""

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_search_input_element(self):
        """获取搜索输入框元素信息"""
        return self.get_by_local.get_element('headline_element', 'search_input')
