def use_exception1():
    while True:
        try:
            num = int(input('请输入一个数字:'))  # 这里报错是：int()函数尝试将这个字符串转换为整数。
            # 但 "abc" 并不是一个合法的数字字符串（它包含非数字字符），因此转换失败。
            print(f'你输入的数字是:{num}')
            break
        except:
            print(f'别输入字母')


def use_exception2():
    '''
    错误类型捕获
    :return:
    '''

    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as e:  # 这一句一般都加上，用来打印异常日志
        print(e)


if __name__ == '__main__':
    # use_exception1()
    use_exception2()
