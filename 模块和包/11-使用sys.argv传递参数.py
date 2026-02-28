import sys

def use_sys_argv(file_path):
    file=open(file_path,mode='w+',encoding='utf-8')
    file.write('好事发生')
    file.close()

if __name__ == '__main__':
    use_sys_argv(sys.argv[1])#用sys.argv[1]去接收传入的参数，参数在上方虫子旁边的三个点那里传入