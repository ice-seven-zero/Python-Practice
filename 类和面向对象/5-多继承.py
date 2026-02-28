class Person:
    def print_name1(self):
        print("person类里的")


class animal:
    def print_name1(self):
        print("animal类里的")


class test01(Person, animal):  # 调用过程是Person->animal->(如还有父类就到父类）
    pass


if __name__ == '__main__':
    jicheng = test01()  # 用到类后面都要加括号
    dongwu = animal()
    jicheng.print_name1()
    dongwu.print_name1()
    print(test01.__mro__)
    print(jicheng.__class__.__mro__)  # __mro__是针对类对象test01的，实例jicheng不可直接调用
