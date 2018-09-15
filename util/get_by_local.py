from util.read_ini import ReadIni
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver
        self.read_ini = ReadIni()

    def element_wait(self, section, option, sec=5):
        """显示等待元素"""
        local = self.read_ini.get_value(section, option)
        if '>' not in local:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = local.split('>')[0].strip()
        local_by = local.split('>')[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(local, sec)
        if by == 'id':
            WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located((By.ID, local_by)), messages)
        elif by == 'name':
            WebDriverWait(self.driver, sec, 0.5).until(
                lambda driver: self.driver.find_element_by_android_uiautomator(local_by).is_displayed(), messages)
        elif by == 'class':
            WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, local_by)),
                                                       messages)
        elif by == 'xpath':
            WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located((By.XPATH, local_by)), messages)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','xpath'.")

    def get_element(self, section, option):
        """获取元素定位信息"""
        local = self.read_ini.get_value(section, option)
        if '>' not in local:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        if by == 'id':
            element = self.driver.find_element_by_id(local_by)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(local_by)
        elif by == 'name':
            element = self.driver.find_element_by_android_uiautomator(local_by)
        elif by == 'elements':
            element = self.driver.find_elements_by_id(local_by)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(local_by)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','xpath'.")
        return element

    def get_toast_element(self, message):
        """获取toast"""
        toast_element = ("xpath", "//*[contains(@text," + message + ")]")
        # 找10秒钟，每0.1秒找一次，找到元素为止
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
