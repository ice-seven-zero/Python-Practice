class woman:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 前面加两个__表示私有属性

    def __secret(self):  # 前面加两个__表示私有方法
        print(f'{self.name}的年龄是{self.__age}')


# 私有属性和私有方法的特点是不能在类外调用

xiaohong = woman('xiaohong', 18)
xiaohong.secret()
