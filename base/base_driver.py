from appium import webdriver
from util.write_user_command import WriteUserCommand
import time
from log.print_log import Log

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "


class BaseDriver:
    def android_driver(self, i):
        # devices_name adb devices
        # port
        write_file = WriteUserCommand()
        device = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        start_t = time.time()
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": device,
            "app": "../data/JZB_7.0.8-website-release.apk",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        try:
            driver = webdriver.Remote('http://localhost:' + port + '/wd/hub', capabilities)
            logger.info(
                "{0} Start Android device <{1}>, Spend {2} seconds".format(success, device, time.time() - start_t))
            time.sleep(10)
            return driver
        except Exception:
            logger.info(
                "{0} Unable to Start Android device <{1}>, Spend {2} seconds".format(fail, device,
                                                                                     time.time() - start_t))

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
