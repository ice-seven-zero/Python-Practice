import re


def single_test01():
    # . 是匹配任意单个字符git
    ret1 = re.match('.', 'y')
    if ret1:
        print(ret1.group())

    ret2 = re.match('w.ll', 'well')
    if ret2:
        print(ret2.group())
    # []是匹配[]内的单个字符
    ret3 = re.match('[w]e', 'well')
    if ret3:
        print(ret3.group())

    ret4 = re.match('[0-9]', '1658')
    if ret4:
        print(ret4.group())  # 只会输出1

    ret5 = re.match(r"\w", '1658')
    if ret5:
        print(ret5.group())

    ret6 = re.match(r"[1-9]?\w$", '09')  # $表示到当前字符串就要结尾了，如果后面还有字符串就会匹配失败
    if ret6:
        print(ret6.group())
    else:
        print('匹配失败')


def multi_test01():
    ret1 = re.match(r'\w[0-9]+', 'y123')
    if ret1:
        print(ret1.group())

    ret2 = re.match(r'[a-zA-Z]+', 'yw123')
    if ret2:
        print(ret2.group())

    names = ["name1", "_name", "2_name", "__name__"]
    for s in names:
        ret3 = re.match(r'[a-zA-Z_]+[\w]*', s)
        if ret3:
            print(f'{ret3.group()}：符合要求')
        else:
            print(f'{s}：不符合要求')


def test01():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang @ qq.com", "xiaohong@qq.com"]
    for s in email_list:
        ret = re.match(r'\w{2,20}@163\.com$', s)  # \.表示对.进行转义，不然默认正则符号.能匹配任意字符
        if ret:
            print(f'邮箱：{ret.group()}是正确')
        else:
            print(f'邮箱：{s}是不正确')
    print('-' * 50)
    for s in email_list:
        ret = re.match(r'\w{2,20}@(163|qq|126)\.com$', s)
        if ret:
            print(f'邮箱：{ret.group()}是正确')
        else:
            print(f'邮箱：{s}是不正确')


if __name__ == '__main__':
    # single_test01()
    # multi_test01()
    # test01()
    # ^在[]内是表示非的意思,()内是一个分组
    ret = re.match(r'([^-]+)-(\d+)', '010-123456')
    if ret:
        print(ret.group())
        print(ret.group(1))
        print(ret.group(2))
    else:
        print('数据有误')
