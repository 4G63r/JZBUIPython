import unittest
import HTMLTestRunner
import multiprocessing
import time
from util.write_user_command import WriteUserCommand
from business.search_business import SearchBusiness
from business.mine_business import MineBusiness
from util.server import Server
import os


class RunCase:
    def test_case01(self):
        case_path = os.getcwd().replace('debug', 'case')
        suite = unittest.defaultTestLoader.discover(case_path, 'test_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
