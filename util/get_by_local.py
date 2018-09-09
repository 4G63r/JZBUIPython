from util.read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, option):
        """获取元素定位信息"""
        read_ini = ReadIni()
        local = read_ini.get_value(section, option)
        if local:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'class':
                return self.driver.find_element_by_class_name(local_by)
            elif by == 'text':
                return self.driver.find_element_by_android_uiautomator(local_by)
            elif by == 'elements':
                return self.driver.find_elements_by_id(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None

    def isElementExist(self, section, option):
        """判断元素是否存在"""
        local_by = self.get_element(section, option)
        if local_by:
            try:
                local_by
                return True
            except:
                return False
        else:
            return None
