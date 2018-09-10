import os

path = os.getcwd()
path1 = path.replace('debug', 'data')
path2 = path1 + '/aaa'
# path1 = os.path.join(path, '123',)
with open(path2, 'w') as f:
    f.write("我爱python1111")
    # f.writelines("北京")
print(path)
print(path2)
