def demo1():
    num1=int(input("请输入一个整数："))
    print('I am demo1')
    return num1

def demo2():
    num2=demo1()
    print('I am demo2')
    return num2

def print_demo3():
    try:
        print(demo2())
    except Exception as e:#打印异常日志
        print(f'未知错误:{e}')

if __name__ == '__main__':
    print_demo3()