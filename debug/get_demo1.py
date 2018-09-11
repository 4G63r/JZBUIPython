from util.read_ini import ReadIni
from log import user_log

logger = user_log.logger


class GetByLocal:

    def get_element(self, section, option):
        """获取元素定位信息"""
        read_ini = ReadIni()
        local = read_ini.get_value(section, option)
        if local:
            try:
                by = local.split('>')[0]
                local_by = local.split('>')[1]
                if by == 'id':
                    return "self.driver.find_element_by_id(" + local_by + ")"
                elif by == 'text':
                    return "self.driver.find_element_by_ui(" + local_by + ")"
            except Exception as e:
                logger.debug(e)
        else:
            return None


if __name__ == '__main__':
    g = GetByLocal()
    print(g.get_element('mine_element', 'mine_tab'))
