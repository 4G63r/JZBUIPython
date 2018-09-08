import yaml


class WriteUserCommand:
    """写入yaml文件"""

    def read_data(self):
        """读取yaml文件数据"""
        with open('/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/config/userconfig.yaml') as fr:
            data = yaml.load(fr)
        return data

    def join_data(self, i, device, bp, port):
        """拼接数据"""
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def write_data(self, i, device, bp, port):
        """写入数据"""
        data = self.join_data(i, device, bp, port)
        with open('/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/config/userconfig.yaml', 'a') as fr:
            yaml.dump(data, fr)

    def clear_data(self):
        """清空数据"""
        with open('/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/config/userconfig.yaml', 'w') as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        """获取配置个数"""
        file_lines = len(self.read_data())
        return file_lines

    def get_value(self, key, port):
        """获取value"""
        data = self.read_data()
        value = data[key][port]
        return value


if __name__ == '__main__':
    w = WriteUserCommand()
    # print(w.get_value('user_info_1', 'bp'))
    print(w.get_file_lines())
    # w.clear_data()
