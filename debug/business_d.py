from handle.mine_handle import MineHandle
from util.get_by_local import GetByLocal
from page.mine_page import MinePage
from log import print_log

logger = print_log.logger


class MineBusiness:
    """我的模块业务交互"""

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        self.mine_handle = MineHandle(driver)
        self.mine_page = MinePage(driver)

    def local_by_log(self, func):
        by = MinePage(func)[1][0]
        local = func[1][0]
        logger.info(str(by) + "定位，操作元素：" + local)

    def go_mine_pass(self):
        """进入我的页面正确"""
        try:
            self.mine_handle.click_mine_tab_element()
            self.local_by_log("self.mine_page.get_mine_tab_element")
            self.mine_handle.click_user_image_element()
            # if self.mine_page.get_sign_button_element() and self.mine_page.get_user_image_element():
            #     return True
            # else:
            #     return False
        except Exception as e:
            logger.error(e)

    def get_driver(self):
        pass
