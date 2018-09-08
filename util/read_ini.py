import configparser
from log.user_log import UserLog

log = UserLog()
logger = log.get_logger()


class ReadIni:
    def __init__(self, file_path=None):
        if file_path == None:
            file_path = '../config/LocalElement.ini'
        self.data = self.read_ini(file_path)

    def read_ini(self, file_path):
        """读取配置文件"""
        # 创建一个读取配置文件的实例
        read_ini = configparser.ConfigParser()
        read_ini.read(file_path)
        logger.debug("读取配置文件到对象")
        log.close_handle()
        return read_ini

    def get_value(self, section, option):
        """通过section和option获取对应的value
        异常的处理，可能会传错误的参数，就返回空
        如果传了错误参数，程序也不应该报错
        """
        try:
            value = self.data.get(section, option)
            logger.debug("输入参数获取定位信息")
            log.close_handle()
        except Exception as e:
            print("传入了错误的参数：%s" % e)
            value = None
        return value


if __name__ == '__main__':
    r = ReadIni()
    print(r.get_value('mine_element', 'user_image1'))
