import os

def use_rename():
    os.rename('.\\目录学习\\123.py','.\\目录学习\\2-改名喽.py')#rename(源文件名，目标文件名)
    #相对路径下改名  .\\表示当前目录  \\是对\的转义


if __name__ == '__main__':
    use_rename()