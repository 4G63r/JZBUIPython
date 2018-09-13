# 需求：有一个杂乱的列表，需要将列表中的每个元素按各自的类型存放到每个对应的列表中，并在控制台打印出这些元素，且保存到当前路径的data文件里
#
# 目的，是将杂乱类型的列表中的所有元素，按数据类型分类后存放到对应的列表中，再将每行数据再存到文件中
#
# 思路：
# 1、首先需要拿到列表中的所有数据类型，将类型存放到list_types列表里
# 2、有重复类型的需要去重，将去重的类型存放到一个新的列表list_types_new中
# 3、以去重后的类型为基准，循环遍历杂乱类型列表中的每个元素(这里需要用到嵌套循环)，每种类型循环一次后清空列表重新遍历下一个类型，循环中打印和写入数据
# 嵌套循环：外层循环控制循环次数，内层循环控制每次需要遍历的个数

# 列表可以存放任意类型的元素，元素间用逗号隔开
list_elements = [1, '1', [1, 2], 3, (3, 'a'), 6.0, {'key1': 'a', 'key2': 3}]
# 1、
list_types = []
for i in list_elements:
    list_types.append(type(i))
# print(list_types)
# [<class 'int'>, <class 'str'>, <class 'list'>, <class 'int'>, <class 'tuple'>, <class 'float'>, <class 'dict'>]
# 2、
list_types_new = list(set(list_types))
# print(list_types_new)
# [<class 'str'>, <class 'tuple'>, <class 'float'>, <class 'dict'>, <class 'int'>, <class 'list'>]
# 3、
lists = []
for j in list_types_new:
    for i in list_elements:
        if isinstance(i, j):
            lists.append(i)
    print(j, lists)
    with open('./data.txt', 'a') as f:
        f.write(str(j) + ' ' + str(lists) + '\n')
    lists.clear()
