for i in range(2000, 2500):
    if i % 5 == 0 and i % 8 == 0:
        print(i)

no = int(input('Enter a number:'))
for i in range(1,11):
    print('%d X %d = %d' %(no, i, no*i))