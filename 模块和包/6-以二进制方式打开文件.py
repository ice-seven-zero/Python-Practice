#binary=二进制
def binary_open():
    file=open('test_binary_file1',mode='rb+')#二进制打开不用指定编码方式
    r=file.read()
    print(r)

    file.close()


if __name__ == '__main__':
    binary_open()