class person(object):
    def __init__(self, color, special, name):
        self.colors = color
        self.special = special
        self.name = name

    def stranger(self):
        print(f'看见生人汪汪叫')

    def family(self):
        print(f'看见家人摇尾巴')


dog1 = person('yellow', 'dog', '大黄')
print(f'一只{dog1.colors}的{dog1.special}叫{dog1.name}')
dog1.stranger()
dog1.family()
print(dog1)  # 默认情况下，会输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
# 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用__str__这个内置方法了
