class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class dog(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def bark(self):
        print("汪汪叫")


class xiaotianquan(dog):
    def __init__(self, name, age, power):
        super().__init__(name, age)  # 在需要的位置使用super().父类方法来调用父类方法的执行
        self.power = power

    def fly(self):
        print("我会飞")


if __name__ == '__main__':
    dahuang = dog('大黄', 18)
    dahuang.drink()
    dahuang.bark()
    xiaotianquan = xiaotianquan("哮天犬", 19, "牛逼")
    print(f'name={xiaotianquan.name},age={xiaotianquan.age},power={xiaotianquan.power}')
    xiaotianquan.sleep()
    xiaotianquan.fly()
