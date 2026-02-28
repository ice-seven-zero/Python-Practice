def demo2(*args, **kwargs):  # 参数名前,增加一个*可以接收元组,参数名前增加两个*可以接收字典
    print(f'demo2的args={args},kwargs={kwargs}')


def demo1(num, *args, **kwargs):  # *args 必须在**kwargs前面
    print(num)
    print(args)
    print(kwargs)
    demo2(*args, **kwargs)  # 调用时,在元组变量前增加一个*，代表元组拆包，在字典变量前增加两个*，代表字典拆包


def demo3(*args):
    num = 0
    for x in args:
        num += x
    return num


if __name__ == '__main__':
    # demo1(1, 2, 3, 4, 5, name='小明', age=18)
    print(demo3(1, 2, 3, 4, 5))
