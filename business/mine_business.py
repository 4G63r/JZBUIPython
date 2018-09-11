from handle.mine_handle import MineHandle
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
from log import user_log

logger = user_log.logger


class MineBusiness:
    """我的模块业务交互"""

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
        self.mine_handle = MineHandle(self.driver)
        # self.mine_page = MinePage(self.driver)

    def go_mine_pass(self):
        """进入我的页面正确"""
        try:
            self.mine_handle.click_mine_tab_element()
            self.mine_handle.click_user_image_element()
            # if self.mine_page.get_sign_button_element() and self.mine_page.get_user_image_element():
            #     return True
            # else:
            #     return False
        except Exception as e:
            logger.error(e)
        finally:
            log.close_handle()

    def get_driver(self):
        driver = self.driver
