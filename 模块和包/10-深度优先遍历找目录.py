import os

def depth_scan1(curren_path):
    '''
    基础版的深度优先遍历找目录
    :param curren_path:
    :return:
    '''
    file_list=os.listdir(curren_path)
    for s in file_list:
        print(s)
        if os.path.isdir(s):
            depth_scan1(s)

def depth_scan2(curren_path,width):
    '''
    改进版的深度优先遍历找目录
    缺陷：os.path.isdir是在当前 Python 程序运行时所在的工作目录里查找名叫 s 的东西
    当前 Python 程序运行时所在的工作目录是：模块和包
    所以能找到文件夹：深度优先找目录
    又因为是先print再进入递归，所以能打印出directory1，但是os.path.isdir(directory1)会是false
    因为directory1不在，模块和包，目录下，所以打印不出directory2

    :param curren_path:
    :return:
    '''
    file_list=os.listdir(curren_path)
    for s in file_list:
        print('-'*width,s)
        if os.path.isdir(s):
            depth_scan2(s,width+4)

def depth_scan3(curren_path,width):
    '''
    终极版，使用os.path.join进行路径拼接,解决os.path.isdir是在当前目录下查找的问题
    :param curren_path:
    :param width:
    :return:
    '''
    file_list = os.listdir(curren_path)
    for s in file_list:
        print('-' * width, s)
        full_path=os.path.join(curren_path,s)#相当于"curren_path" + "/" + "s"
        if os.path.isdir(full_path):
            depth_scan3(full_path,width+4)#这里要传入full_path,这样后续的路径才能拼接



if __name__ == '__main__':
    #depth_scan1('.')
    #depth_scan2('.',0)
    depth_scan3('.',0)