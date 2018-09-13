import logging
import os
import time

# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG
logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
file_handle = logging.FileHandler(path, 'a', encoding='utf-8')
# 添加日志格式
formatter = logging.Formatter(
    '%(asctime)s %(filename)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s')
file_handle.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(file_handle)


def close_handle():
    logger.removeHandler(file_handle)
    file_handle.close()
