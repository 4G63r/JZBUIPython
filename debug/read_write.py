import os

path = os.getcwd()
path1 = os.path.join(path, '123')
# with open(path1, 'w') as f:
#     # f.write()
#     f.writelines("北京")
# print(path)
# print(path1)

with open(path1) as f1:
    print(f1.read(1))
