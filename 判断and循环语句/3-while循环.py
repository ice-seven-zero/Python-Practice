i = 1
while i < 5:
    i += 1  # python里没有i++，可以i=i+1
print(f'输出i的值为{i}')

row = 1
while row < 5:
    print('*' * row)
    row += 1

# print自动换行问题
print('hello world', end='  ')
print('python')
