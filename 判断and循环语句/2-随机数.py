import random  # 表示引用random这个包

computer = random.randint(1, 3)
a = int(input("1、剪刀 2、石头 3、布\n请输入你的答案："))
if (a == 1 and computer == 3) or (a == 2 and computer == 1) or (a == 3 and computer == 2):
    print('你赢了')
elif (a == computer):
    print('平局')
else:
    print('电脑赢了')
