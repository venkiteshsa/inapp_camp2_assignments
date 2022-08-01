
num, x, y = 1, 1, 1
n = int(input('Enter the no. of rows for your Floyd\'s triangle:'))

for x in range(n+1):
    for y in range(x):
        print(num, end=" ")
        num = num + 1
    print('\n')
