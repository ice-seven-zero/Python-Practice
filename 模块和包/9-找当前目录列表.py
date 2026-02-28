import os


def use_dir_func():  # dir 是 directory 的简写，表示“目录”。
    file_list = os.listdir('.')  # '.'表示找当前目录下的文件名
    for s in file_list:
        print(s)


if __name__ == '__main__':
    use_dir_func()
