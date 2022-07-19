import sys
from tkinter.ttk import Separator
import re
"""
print('Hello world')
print(sys.version)
make = 'Dell'
dollarRate = 70.256
myText = 'The amount for this %s computer is %d USD and the exchange rate is %4.2f USD to 1 INR' %(make,1299, dollarRate)
print(myText)
myText1 = '{0} is easier than {1}'.format('Python', 'Java')
print(myText1)
print('{0} is my country. All {0}ns are my brothers and sisters'.format('India').count('India'))

myString = 'superman'
print(myString.endswith('man'))
print(myString.endswith('man', 3))
print(myString.endswith('man', 2, 6))
print(myString.endswith(('man', 'ma'), 2, 6))
print('Postman'.endswith(('man', 'ma'), 2, 6))

print('Hello Good Morning'.find('Go'))
print('Hello Good Morning'.find('Go', 4))
print('Hello Good Morning'.find('Go', 4, 15))
print('Hello Good Morning'.find('kk'))


'Hello'.lower()
Separator = '*'
myTuple = ('H','e', 'l', 'l', 'o')
print(Separator.join(myTuple))

newString = 'Hello world'
newString = newString.replace('o', 'i')
print(newString)
myStringSplit = newString.split(' ')
print(myStringSplit)


# REGEX
txt = 'bits of paper bits of paper'
x = re.findall('bi', txt)
print(x)
x = re.search('bi', txt)
print(x)
x = re.sub(" ", "-", txt)
print(x)

txt = "Hello World"
x = re.findall("[a-m]", txt)
print(x)

txt = "James Bond is 007"
x = re.findall("\d", txt)
print(x)

txt = "Hello World"
x=re.findall("He..o", txt)
print(x)

txt = "hello world"
x = re.findall("^hello", txt)
print(x)

x = re.findall('world$', txt)
print(x)




txt = "James invented Watt the "
x = re.findall(r"\bthe", txt)
print(x)

txt = "James watt invented sothe"
x = re.findall(r"the$", txt)
print(x)

txt = "James watt invented the "
x = re.findall(r"\AJames", txt)
print(x)



myString = 'my email is abhi@abhi.com hope you will note it down'

regex = r'\S+@\S+'
x = re.findall(regex, myString)
print(x)


studentsAge = [18, 21, 23, 20, 21]
print(studentsAge)
print(studentsAge[2])
newStudentsAge = studentsAge[2:4]
print(newStudentsAge)
newStudentsAge = studentsAge[1:5:2]
print(newStudentsAge)
newStudentsAge = studentsAge[:3]
print(newStudentsAge)
newStudentsAge = studentsAge[::-1]
print(newStudentsAge)
newStudentsAge = studentsAge[-2]
print(newStudentsAge)


studentsAge.append(20)
studentsAge.append('hi')
print(studentsAge)
del studentsAge[-1]
print(studentsAge)

studentName = ['Anu', 'Sinu', 'Binu']
studentsAge.extend(studentName)
print(studentsAge)

print('Anu' in studentName)
print('Anushka' in studentName)

print(len(studentName))

studentName.reverse()
print(studentName)
studentName.reverse()
print(studentName)

studentName.sort()
print(studentName)

print(studentName*3)


#tuples are immutable
months = ('Jan', 'Feb', 'Mar')
print(months[0])
print(months[-1])
print(len(months))
print('Jan' in months)
print(months+months)
print(months*3)


myStudents = {'Abhi':1, 'Sibi':2}
print(myStudents)
myStudents = dict(Abhi=30, Sibi=28)
print(myStudents)
myStudents = dict({'Abhi':20, 'Sibi':10})
print(myStudents)

print(myStudents.get('Sibi'))
print(myStudents.items())
print(myStudents.keys())
print(myStudents.values())


months = {'Jan', 'Feb', 'Mar'}
months = set(['Jan', 'Feb', 'Mar'])
print(months)
print(type(months))

for i in months:
    print(i)

for i in months:
    print(type(i))

days = set()
days.add('Mon')
days.add('Tue')
days.add('Wed')

for i in days:
    print(i)

days.update(['Thur', 'Fri'])

for i in days:
    print(i)

days.discard('Thur')
print(days)


months1 = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'}
months2 = {'Mar', 'Apr', 'May', 'Feb'}
months3 = {'Feb', 'Mar', 'Jun', 'Jul'}

print(months1 > months2)
print(months1 < months3)
print(months2 == months3)
print(months1 >= months2)
print(months1 <= months2)

months4frozen = frozenset({'Nov', 'Dec'})
print(type(months4frozen))
print(months4frozen)

studName = input("Please enter your name:")
studAge = int(input("Please enter your age:"))
print("The student name is", studName, "and the age is", studAge)
print("The student name is %s and the age is %d" %(studName, studAge))
print("The student name is {} and the age is {}".format(studName, studAge))
print('''Hello %s
How are you''' %studName)
print('You are over 20\nSo you are eligible')

#Control flow statements
#Conditional statements
#If condition
userInputNo = input('Enter either 1 or 2 :')
if userInputNo == '1':
    print('You entered 1')
elif userInputNo == '2':
    print('You entered 2')
else:
    print('Wrong input')

#Inline if statement
b = 12
a = 12 if b == 10 else 13
print(a)

print('b is ten' if b == 10 else 'b is not 10')


#Match case

def http_status(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Page not found'
        case _:
            return 'Unknown error occured'

print(http_status(404))


#Looping
#For loop

fruits = ['apples', 'oranges', 'banana', 'cherry']

for i in fruits:
    print(i)

for i, j in enumerate(fruits):
    print(i, j)

for i in range(10):
    print(i)


#while loop

counter = 5
while counter > 0:
    print("Counter =", counter)
    counter = counter - 1

#break and continue

j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ',j)
    if j == 6:
        break

j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j == 6:
        continue
    print('j value is ', j)


#Functions

def findSum(a,b):
    sum = a+b
    return sum

print(findSum(2,3))

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if numberToCheck%x == 0:
            return False
        return True

print(checkIfPrime(11))



def calculations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return(add, sub, mul, div)
output = calculations(40, 30)
print("Addition = ", output[0])
print("Subtraction = ", output[1])
print("Multiplication = ", output[2])
print("Division = ", output[3])

"""

def calculate(a, b):
    add = a + b
    yield add
    sub = a - b
    yield sub
    mul = a * b
    yield mul
    div = a % b
    yield div
for value in calculate(40, 30):
    print(value)
