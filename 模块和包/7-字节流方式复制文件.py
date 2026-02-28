
def copy_open():
    file1=open('壁纸1.jpg',mode='rb+')
    file2=open('复制壁纸1.jpg',mode='wb+')
    test=file1.read()
    file2.write(test)
    file1.close()
    file2.close()


if __name__ == '__main__':
    copy_open()
