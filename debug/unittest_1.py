import os
import unittest
import HTMLTestRunner
import HTMLTestRunnerNew
import time
from debug.base_d import Base_d
from debug.business_d import MineBusiness
from log import my_log

logger = my_log.logger


class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass----->")
        cls.driver = Base_d()
        cls.mine_business = MineBusiness(cls.driver)

    def setUp(self):
        print("this is setup")

    def test_01(self):
        '''成功进入搜索页面'''
        flag = self.mine_business.go_mine_pass()
        try:
            self.assertTrue(flag, msg="进入搜索页面测试不通过")
        except:

            my_log.logger("")

    def tearDown(self):
        print('this is teardown')
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_name = os.getcwd().replace('case', 'result/screenshot/') + case_name + '.png'
                self.driver.save_screenshot(file_name)

    @classmethod
    def tearDownClass(cls):
        print('this is class teardown')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01'))
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    base_path = os.getcwd().replace('debug', 'result/report/')
    file_path = base_path + now + '.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='自动化测试报告', description='xx')
        # runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title='自动化测试报告', description='产品靠大家，质量你我他！',
        #                                           tester='宋宵')
        runner.run(suite)
