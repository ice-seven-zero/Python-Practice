# eval是将字符串 当成有效的表达式 来求值 并返回计算结果

def test_eval1():
    '''
    读取文件，测试eval
    :return:
    '''
    file = open('eval_test_file', 'r+', encoding='utf-8')
    test=file.read()
    print(test)
    print(type(test))#此时<class 'str'>
    file.close()

def test_eval2():
    '''
    读取文件，测试eval
    :return:
    '''
    file = open('eval_test_file', 'r+', encoding='utf-8')
    test=eval(file.read())#文件里存储的是字典的字符串表示形式，eval将其还原成了字典对象并执行
    print(test)
    print(type(test))#此时<class 'dict'>
    file.close()
#eval在王道课程里只用于读配置（文件）

if __name__ == '__main__':
    #test_eval1()
    test_eval2()