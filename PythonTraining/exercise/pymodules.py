"""

import random as r
print(r.randrange(1, 10))
print(r.random())
print(r.randint(5, 20))
print(r.choice(["head", "tail"]))
myShirtColors = ["blue", "red", "black", "yellow", "green"]
r.shuffle(myShirtColors)
print(myShirtColors)

r.seed(11)
print(r.random())

import time
print(time.time()) #seconds past 1st jan 1970
print(time.localtime(time.time())) #get the multiple time value as a tuple
print(time.asctime(time.localtime(time.time())))

for i in range(0, 10):
    print(i)
    time.sleep(1)#delay the program execution by the specified no. of seconds



import datetime
from tkinter.messagebox import YES
print(datetime.datetime.now())

mydate = datetime.datetime(2020, 5, 4)
print(mydate)
mydate = datetime.datetime(2020, 5, 4, 10, 15, 40) #with time
print(mydate)

from datetime import datetime as dt

if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
    print("Working hours....")
else:
    print("Shift completed")

import calendar

myCalendar = calendar.month(2022, 7)
print(myCalendar)
myCalendar = calendar.prcal(2022)
print(myCalendar)

import math
#finding the exponential of a number, then its absolute, then its log, then convert to the base of 10
number = 2e-7 #small value of x
print(math.log(math.fabs(number), 10))

number = 7e-2
print('The given number (x) is :', number)
print('e^x (using exp() function) is :', math.exp(number)-1)

number = math.pow(4,2)
print(number)
number = math.floor(4.2)
print(number)
number = math.ceil(4.3)
print(number)
number = math.fabs(-10)
print(number)
number = math.factorial(10)
print(number)
number = math.modf(3.14)
print(number)

#custom module
import prime
n = int(input("Enter a number:"))
if prime.checkIfPrime(n):
    print("It is a prime number")
else:
    print("It is not a prime number")

"""

