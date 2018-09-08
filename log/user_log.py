import logging
import os
import time


class UserLog:
    """日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG"""

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 创建handler输出日志到控制台
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        # console.close()
        # logger.removeHandler(console)

        # 创建文件路径
        base_path = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(base_path, 'test_log')
        now_time = time.strftime('%Y-%m-%d')
        path = log_path + '/' + now_time + '.log'

        # 创建handler输出日志到文件
        self.file_handle = logging.FileHandler(path, 'a', encoding='utf-8')
        # 添加日志格式
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(self.file_handle)

    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    u = UserLog()
    log = u.get_logger()
    log.debug("调试")
    log.error("只是错误")
    log.critical("完蛋了")
    u.close_handle()
