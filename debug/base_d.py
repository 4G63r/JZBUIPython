from appium import webdriver


class Base_d:
    def get_driver(self):
        """获取driver"""
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            # "deviceName": "192.168.56.101:5555",
            # "deviceName": "83e54a4c384e4a31",
            "deviceName": "ac05b72c",
            "app": "/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/data/JZB_7.0.8-website-release.apk",
            # "appWaitActivity": "com.eduu.bang.app.SplashActivity",  # 需要等待切换activity(真机常见问题)
            "noReset": "true",  # 不用每次启动都重置应用
            "unicodeKeyboard": "true",  # 使用unicode编码方式发送字符串
            "resetKeyboard": "true"  # 是否重置键盘
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        return driver
