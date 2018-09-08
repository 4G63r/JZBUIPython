from util.dos_cmd import DosCmd


# windows → netstat -ano | findstr 4723
# mac → lsof -i:4723
class Port:
    def port_is_used(self, port_num):
        """判断端口是否被占用"""
        flag = None
        self.dos = DosCmd()
        result = self.dos.execute_cmd_result('lsof -i:' + str(port_num))
        if len(result) > 0:
            flag = False  # 被占用
        else:
            flag = True  # 没被占用
        return flag

    def create_port_list(self, start_port, device_list):
        """生成可用端口"""
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            print('Failed to connect devices and generate ports...')
            return None


if __name__ == '__main__':
    port = Port()
    li = [1, 2]
    print(port.create_port_list(4700, li))
