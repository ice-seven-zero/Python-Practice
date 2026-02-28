def open_file1():
    #open文件时，文件名需要注意大小写
    file=open('text_file1.txt',mode='r',encoding='utf-8')#mode表示打开的模式，encoding表示打开的编码方式
    print(file.read())
    file.close()

def write_file2():
    file=open('text_file2.txt',mode='w',encoding='utf-8')#w是直接写覆盖或创建文件
    file.write('坚持学习')
    file.close()

def open_rj():
    file1=open('text_file1.txt',mode='r+',encoding='utf-8')
    file1.write('嗨嗨嗨')
    file1.close()


def open_aj():
    file2=open('text_file1.txt',mode='a',encoding='utf-8')
    file2.write('嗨嗨嗨')#a和r+的区别是：a是在末尾写，r+是在开头写
    file2.close()



if __name__ == '__main__':
    #open_file1()
    #write_file2()
    #open_rj()
    open_aj()