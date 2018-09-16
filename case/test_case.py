import os
import unittest
import HTMLTestRunner
import multiprocessing
import time
from base.base_driver import BaseDriver
from log.print_log import Log
from util.write_user_command import WriteUserCommand
from business.mine_business import MineBusiness
from util.element_action import ElementAction
from util.server import Server


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BaseDriver().android_driver(i)
        cls.ea = ElementAction(cls.driver)
        cls.mb = MineBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def setUp(self):
        self.logger = Log()
        self.logger.info("----------------------------------------------------------------")
        self.logger.info("################################ START ################################")

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_name = os.getcwd().replace('case', 'result/screenshot/') + case_name + '.png'
                self.ea.take_screenshot(file_name)
        self.logger.info("################################  END  ################################")

    def test_01_go_mine(self):
        """
        1、点击"我的"
        2、进入"我的"页面
        3、以头像和签到元素是否存在为验证条件
        """
        flag = self.mb.go_mine_pass()
        self.assertTrue(flag)

    def test_02_loginRegister_panel(self):
        """
        1、以游客判断登录状态，如果是游客身份
        2、点击好友、收藏、签到、孩子档案、我的发表、课程订单、成长记录会弹登录注册框
        3、以是否弹框为验证条件
        """
        flag = self.mb.test_loginRegister_panel()
        self.assertTrue(flag)

    def test_03_loginRegister_panel(self):
        """
        1、以游客判断登录状态，如果是游客身份
        2、点击好友、收藏、签到、孩子档案、我的发表、课程订单、成长记录会弹登录注册框
        3、以是否弹框为验证条件
        """
        pass


def appium_init():
    server = Server()
    server.main()


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


def get_suite(i):
    print("get_suite里面的", i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01_go_mine', parame=i))
    suite.addTest(CaseTest('test_02_loginRegister_panel', parame=i))
    # suite.addTest(CaseTest('test_03', parame=i))

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    base_path = os.getcwd().replace('case', 'result/report/')
    file_path = base_path + now + str(i) + '.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='自动化测试报告',
            description='JZB_App_v7.0.8_testcase\nTester: 宋宵'
        )
        runner.run(suite)


if __name__ == '__main__':
    appium_init()
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite, args=(i,))
        t.start()
