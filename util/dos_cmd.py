import os


# os.system()不能收集结果
# print(os.system('adb devices'))
# os.popen()可以收集结果
# ['List of devices attached\n', 'ac05b72c\tdevice\n', '\n']
class DosCmd:
    def execute_cmd_result(self, command):
        """收集设备信息"""
        result_list = []
        result = os.popen(command).readlines()
        # print(result)
        for i in result:
            if 'List of devices' in i or i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def execute_cmd(self, command):
        """不需要收集直接执行命令"""
        os.system(command)


if __name__ == '__main__':
    dos_cmd = DosCmd()
    # print(dos_cmd.execute_cmd_result('ps -ef|grep node'))
    print(dos_cmd.execute_cmd_result('adb devices'))
