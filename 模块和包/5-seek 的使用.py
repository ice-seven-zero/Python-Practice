import os

def use_seek():
    file=open('test_file3.txt',mode='w+',encoding='utf-8')
    file.write('123  hello')
    file.seek(5,os.SEEK_SET)#光标移动到5
    print(file.read(3))
    #print(type(file))
    file.close()

if __name__ == '__main__':
    use_seek()