# 需求：封装一个可以复用的类，作用是输入终端命令就能拿到想要的返回值
# 比如调用这个类时传入"adb devices"就能拿到设备名
# 提示：os.popen(command)用os下面的popen()函数进行逐步封装
# 可以先执行下os.popen('adb devices')看看返回的是什么，然后再对返回值进行处理最后拿到想要的设备名

import os


class DosCmd:
    def execute_cmd_result(self, command):
        """收集设备信息"""
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if 'List of devices' in i or i == '\n':
                continue
            result_list.append(i.strip('\n').split('\t')[0])
        return result_list

    def execute_cmd(self, command):
        """不需要收集直接执行命令"""
        os.system(command)


if __name__ == '__main__':
    dos_cmd = DosCmd()
    print(dos_cmd.execute_cmd_result("adb devices"))
