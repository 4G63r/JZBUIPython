import os
import unittest
import HTMLTestRunner
import HTMLTestRunnerNew
import time
from util.get_by_local import GetByLocal
from log.user_log import UserLog


class CaseTest(unittest.TestCase):
    @classmethod  # 容器 java里叫注解
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_logger()
        print("setupclass----->")
        # cls.search_business = SearchBusiness(i)
        cls.mine_business = GetByLocal(1)

    def setUp(self):
        print("this is setup")

    def test_01(self):
        '''成功进入搜索页面'''
        self.mine_business.get_element('mine_element', 'user_image1')
        self.logger.debug("正在定位一个元素")

    def tearDown(self):
        print('this is teardown')

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        print('this is class teardown')
        # cls.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01'))
    # suite.addTest(CaseTest('test_02', parame=i))
    # suite.addTest(CaseTest('test_03', parame=i))
    # suite.addTest(CaseTest('test_04', parame=i))
    # suite.addTest(CaseTest('test_05', parame=i))
    # suite.addTest(CaseTest('test_01'))
    # unittest.TextTestRunner().run(suite)

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    base_path = os.getcwd().replace('debug', 'result/report/')
    file_path = base_path + now + '.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='自动化测试报告', description='xx')
        # runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title='自动化测试报告', description='产品靠大家，质量你我他！',
        #                                           tester='宋宵')
        runner.run(suite)
