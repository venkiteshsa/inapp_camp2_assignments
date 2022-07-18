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



"""

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

