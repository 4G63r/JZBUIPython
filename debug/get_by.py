from util.read_ini import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_local(self, section, option):
        """获取定位方式"""
        read_ini = ReadIni()
        local = read_ini.get_value(section, option)
        if local:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            return by, local_by
        else:
            return None

    def get_element(self, section, option):
        """获取元素定位信息"""
        if self.get_local(section, option):
            by = self.get_local(section, option)[0]
            local_by = self.get_local(section, option)[1]
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
        flag = False
        try:
            self.get_element(section, option)
            flag = True
        except:
            flag = False
        return flag