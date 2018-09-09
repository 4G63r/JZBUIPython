import configparser

a = configparser.ConfigParser()
a.read("/Volumes/SAMSUNG/FF_RUSH/jiazhangbang/config/LocalElement.ini")
b = a.get('mine_element', 'user_image1')
print(b)