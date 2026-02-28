age = int(input('请输入你的年龄:'))  # 因为input的输入默认是字符型，所以要强制类型转换
if 18 <= age <= 60:
    print('允许进入')
else:
    print('不得进入')
