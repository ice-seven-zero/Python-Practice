def To_Multiply(temp1, temp2):
    print(temp1 * temp2)


if __name__ == '__main__':  # 这段话可以让别的文件调用这个模块时，下面的内容不运行
    # 打个main就会自动弹出来
    print(f'此时__name__是：{__name__}')
    a = 2
    b = 2  # 里面定义的这两个变量仍是全局变量
    To_Multiply(a, b)
    # 本质是别的文件调用这个模块时，这个模块的__name__会变成my_first_mode
    # 但该模块自己调用时，__name__==__main__

    # 下面这个没框住，别的文件调用这个模块时还会运行
print(f'my_first_mode.__name__是：{__name__}')
