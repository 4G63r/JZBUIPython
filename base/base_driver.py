from appium import webdriver
from util.write_user_command import WriteUserCommand
import time


class BaseDriver:
    def android_driver(self, i):
        # devices_name adb devices
        # port
        print("this is android_driver:", i)
        write_file = WriteUserCommand()
        device = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": device,
            "app": "../data/JZB_7.0.8-website-release.apk",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        driver = webdriver.Remote('http://localhost:' + port + '/wd/hub', capabilities)
        time.sleep(10)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
