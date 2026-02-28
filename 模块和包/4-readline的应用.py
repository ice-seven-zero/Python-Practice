def open_readline():
    file=open('text_file1.txt',mode='r+',encoding='utf-8')
    while True:
        line=file.readline()
        if not line:#当file.readline()读取到文件末尾（EOF）时，它会返回一个空字符串 '',被视为 False
            break
        print(line,end='')#因为print自带换行，但readline也有换行，所以用end=''取消print的换行
    file.close()

if __name__ == '__main__':
    open_readline()