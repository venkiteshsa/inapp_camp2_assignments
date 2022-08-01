currency = {2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

N = int(input("Enter the amount:"))
n = N

for i in currency.keys():
    if n != 0:
        currency[i] = n // i
        n = n % i

for i in currency.keys():
    if currency[i] != 0:
        print('%d : %d' % (i, currency[i]))