def func(num):
    if num == 1:
        return num
    return num + func(num - 1)


if __name__ == '__main__':
    print(func(5))
