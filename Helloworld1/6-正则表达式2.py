import re


# 扫描整个字符串与re.match不同，search不要求匹配必须从字符串开头开始。
# 它会在字符串中任意位置查找第一个符合条件的子串。
# 返回第一个匹配：一旦找到第一个匹配，就会停止搜索，返回该匹配对象。


def search_use():
    ret = re.search(r"\d+", "abc999")
    print(ret.group())


if __name__ == '__main__':
    search_use()
