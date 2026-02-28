# 单例模式是指让类创建的对象，在系统中只有唯一的一个实例，也就是把类这个可变数据类型改成不可变数据类型
class player(object):
    instance = None#不一定是instance，随便个其他的例如 ppinstance 也行

    def __new__(cls, *args, **kwargs):#self:实例方法,实例本身    cls:类方法,类本身
        if player.instance is None:
            player.instance = super().__new__(cls)  # 固定写法，调用其父类，即object的__new__

        return player.instance
        # __new__相当于c语言中的malloc
        # 上面代码的意思是：如果是第一次调用这个类，就给分配地址，否则就一直用第一次分配的地址

    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    xiaoming=player('小明')
    xiaohong=player('小红')
    print(id(xiaoming))
    print(id(xiaohong))
    print(xiaoming.name)
