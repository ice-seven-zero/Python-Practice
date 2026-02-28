"""
 短路运算的目的是懒得写if
 and是遇假则假，都真返回后一个
 or是遇真则真，否则返回前一个
"""
a = False
a and print('hello and')
a or print('hello or')
print(5 << 1)  # 5左移一位
print(-5 << 1)
print(-2 >> 1)  # 左移乘2，右移除2
