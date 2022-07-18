import sys

print('Hello world')
print(sys.version)
make = 'Dell'
dollarRate = 70.256
myText = 'The amount for this %s computer is %d USD and the exchange rate is %4.2f USD to 1 INR' %(make,1299, dollarRate)
print(myText)
myText1 = '{0} is easier than {1}'.format('Python', 'Java')
print(myText1)
print('{0} is my country. All {0}ns are my brothers and sisters'.format('India').count('India'))