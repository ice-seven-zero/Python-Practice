def nochange_test(a1):  # 不可变数据类型
    print('-' * 50)
    print(f'a1在函数内的内存地址是:{id(a1)}')
    result = 100
    print(f'result在函数内的内存地址是:{id(result)}')
    print('-' * 50)
    return result


# a1 = 10
# print(f'调用函数前,a1内存地址是:{id(a1)}')  # 因为变量和数据是分开存储的，所以10所在的内存地址是不变的
# b1 = nochange_test(a1)
# print(f'test返回值的内存地址是:{id(b1)}')


def change_test(list1):  # 可变数据类型
    print(f'修改数据前的地址为：{id(list1)}')
    list1[0] = 10
    print(f'可变数据类型是直接修改里面的值，原数据的地址不变，修改数据后的地址为：{id(list1)}')
    list1 = [5, 6, 7]
    print(f'此时地址就不同了，为：{id(list1)}')


# 通过接口改变的是数据所在的位置，变量的地址没变

list2 = [1, 2, 3, 4, 5]
change_test(list2)
print(list2)
print(f'list2的地址为：{id(list2)}')
