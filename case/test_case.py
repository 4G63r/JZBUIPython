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

    def setUp(self):
        self.logger = Log()
        self.logger.info("----------------------------------------------------------------")
        self.logger.info("################################ START ################################")

    def tearDown(self):
        time.sleep(2)
        self.ea.click_deviceBtn(4)
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
        3、以头像和签到元素以及登录文案是否存在为验证条件
        """
        flag = self.mb.go_mine()
        self.assertTrue(flag, "进入'我的'页面测试不通过")

    def test_02_user_image(self):
        """
        1、检查是否为游客身份
        2、如果是游客，点击头像进入手机号登录页
        3、如果是已登录状态，点击头像会跳转到用户资料页面
        """
        flag = self.mb.user_image()
        self.assertTrue(flag, "点击我的头像跳转测试不通过")

    def test_03_friend(self):
        """
        1、检查是否为游客身份
        2、如果是游客，点击好友弹出登录注册框
        3、如果是已登录状态，点击好友跳转到好友页面
        """
        flag = self.mb.friend()
        self.assertTrue(flag, "点击好友跳转测试不通过")

    def test_04_collect(self):
        """
        1、检查是否为游客身份
        2、如果是游客，点击收藏弹出登录注册框
        3、如果是已登录状态，点击收藏跳转到收藏页面
        """
        flag = self.mb.collect()
        self.assertTrue(flag, "点击收藏跳转测试不通过")

    def test_05_notice(self):
        """
        1、点击消息跳转到消息页面
        2、以发信、帮通知、通知元素是否存在判断页面跳转
        """
        flag = self.mb.notice()
        self.assertTrue(flag, "点击消息跳转测试不通过")

    def test_010_loginRegister_panel(self):
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
    suite.addTest(CaseTest('test_02_user_image', parame=i))
    suite.addTest(CaseTest('test_03_friend', parame=i))
    suite.addTest(CaseTest('test_04_collect', parame=i))
    suite.addTest(CaseTest('test_05_notice', parame=i))

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
