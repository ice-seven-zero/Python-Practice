mylist = ['ab', 'cd', 'ef', 'gh']
for i in mylist:
    print(i, end='  ')
print('')
print('-' * 50)
for p in range(1, 10):  # range是左闭右开的
    if p == 8:
        print('找到8')
        break
else:
    print('未找到')  # else 子句：当循环正常结束（没有被 break 中断）时执行，不是必须的
