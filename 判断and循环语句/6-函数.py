def say_hello():  # def=define
    print('Hello World!')
    print('Hello python!')


print('不调用函数，函数是不会执行的')
say_hello()


def sum_2_num(num1, num2):
    result = num1 + num2
    print(f'两数相加的结果是:{result}')
    return result  # 如果不写return，则默认返回None


a = sum_2_num('ab', 'cd')
print(f'a的结果是={a}')
