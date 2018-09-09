import configparser
from log.user_log import UserLog


class ReadIni:
    def __init__(self, file_path=None):
        self.log = UserLog()
        self.logger = self.log.get_logger()
        if file_path == None:
            file_path = '../config/LocalElement.ini'
        self.data = self.read_ini(file_path)

    def read_ini(self, file_path):
        """读取配置文件"""
        # 创建一个读取配置文件的实例
        read_ini = configparser.ConfigParser()
        read_ini.read(file_path)
        return read_ini

    def get_value(self, section, option):
        """通过section和option获取对应的value
        异常的处理，可能会传错误的参数，就返回空
        如果传了错误参数，程序也不应该报错
        """
        try:
            value = self.data.get(section, option)
        except Exception as e:
            self.logger.error(e)
            self.log.close_handle()
            value = None
        return value


if __name__ == '__main__':
    r = ReadIni()
    r.get_value('mine_element', 'user_image1')
