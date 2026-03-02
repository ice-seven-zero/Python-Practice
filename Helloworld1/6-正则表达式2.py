import re


# 扫描整个字符串与re.match不同，search不要求匹配必须从字符串开头开始。
# 它会在字符串中任意位置查找第一个符合条件的子串。
# 返回第一个匹配：一旦找到第一个匹配，就会停止搜索，返回该匹配对象。


def search_use():
    ret = re.search(r"\d+", "abc999")
    print(ret.group())


def findall_use():  # findall是生成所有
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)  # findall的结果已经是可直接使用的数据，不需要（也不能）调用 group()


def sub_use1():  # sub的作用是将数据进行替换
    s = 'hello world, now is 2020/7/20 18:48 ,现在是 2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日|分', r' ', ret_s)
    ret_s = re.sub(r'时', r':', ret_s)
    print(ret_s)


def sub_use2():
    long_text = """<p>岗位职责：</p><p>完成推荐算法、数据统计、接口、后台等服务器端相关工作
         </p><p><br></p><p>必备要求：</p>
         <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
         < p >& nbsp; < br > < / p >
         < p > 技术要求： < / p >
         < p > 1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式 < / p >
         < p > 2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架 < / p >
         < p > 3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL / PostgreSQL 中的一种 <
         br > < / p >
         < p > 4、掌握NoSQL、MQ，熟练使用对应技术解决方案 < / p >
         < p > 5、熟悉 Javascript / CSS / HTML5，JQuery、React、Vue.js < / p >
         < p > & nbsp; < br > < / p >
         < p > 加分项： < / p >
         < p > 大数据，数理统计，机器学习，sklearn，高性能，大并发。 < / p > """
    print(re.sub(r'<[^>]*>|& nbsp;|\n|\s', '', long_text))


def split_use():  # split 根据匹配进行切割字符串，并返回一个列表
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


def greedy_test():
    s = "This is a number 234-235-22-423"
    r = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(r.group(1))


def option_use():
    print(re.match(r"\w*", "abc你好").group())
    print(re.match(r"\w*", "abc你好", flags=re.A).group())  # re.A 不让\w 匹配汉字
    print(re.match("a*", "aA").group())
    print(re.match("a*", "aA", flags=re.I).group())  # re.I 是否区分大小写
    print(re.match(".*", "abc\ndef").group())
    print(re.match(".*", "1abc\ndef", flags=re.S).group())  # re.S 可以让.匹配上\n


if __name__ == '__main__':
    # search_use()
    # findall_use()
    # sub_use1()
    # sub_use2()
    # split_use()
    # greedy_test()
    option_use()
