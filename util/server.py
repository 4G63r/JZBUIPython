import time

from util.dos_cmd import DosCmd
from util.port import Port
import multiprocessing
from util.write_user_command import WriteUserCommand


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        """获取设备信息"""
        devices_list = []
        result_list = self.dos.execute_cmd_result('adb devices')
        if len(result_list) >= 1:
            for i in result_list:
                if 'daemon' in i or 'offline' in i or 'unauthorized' in i:
                    print("❗️❗❗Device Not Found❗❗❗")
                    continue
                devices_list.append(i.split('\t')[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """创建可用端口"""
        port = Port()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        # appium -p 4700 -bp 4900 -U deviceName
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + \
                  self.device_list[i] + ' --no-reset --session-override'
        command_list.append(command)
        self.write_file.write_data(i, self.device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    def start_server(self, i):
        """启动服务"""
        self.start_list = self.create_command_list(i)
        print(self.start_list)
        self.dos.execute_cmd(self.start_list[0])

    def main(self):
        """多线程启动appium"""
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(8)

    def get_process_pid(self, command):
        """获取程序进程pid
        window → tasklist | find "node.exe"
        mac → ps -ef | grep node
        """
        pid_list = []
        process_list = self.dos.execute_cmd_result(command)
        if len(process_list) > 2:
            for i in range(2, len(process_list)):
                pid = process_list[i].split()[1]
                pid_list.append(pid)
            return pid_list
        else:
            return None

    def kill_server(self):
        """杀掉进程
        window → taskkill -F -PID node.exe
        mac → kill -9 pid
        """
        process_list = self.get_process_pid('ps -ef | grep node')
        if process_list:
            for i in process_list:
                self.dos.execute_cmd('kill -9 ' + i)
                print("---PID " + i + ' node进程清理完成---')
        else:
            print("---appium没有启动不需要清理---")


if __name__ == '__main__':
    server = Server()
    # print(server.get_devices())
    # print(server.create_port_list(4700))
    server.main()
    # print(server.get_process_pid('ps -ef | grep node'))
    # server.kill_server()
