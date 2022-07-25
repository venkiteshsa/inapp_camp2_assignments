#File handling
"""

#trying to open a file myfile.txt in the same dir
#using open() method get the file object

myFile = open("myfile.txt", "r")
 
#to read the contents, use the read() method

#print(myFile.read(10))
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())



#A simple example for higher order function
#which can accept at least one fn and can optionally return a fn

#a simple fn with a print statement
def greet(name):
    return "Hello {}".format(name)

#defining the higher order fn which can accept fn
def print_greetings(fn, param):
    print(fn(param))

#calling the higher order fn
print_greetings(greet, 'Abhi')


#map function
#a higher order fn which can accept a fn and also a list of iterable params.
#each param will be applied to the fn and result will be returned back as a map obj.
#we can later convert this map obj into set/tuple


def mymapfunction(a):
    return a*a

x = map(mymapfunction, (1,2,3,4,5))
print(tuple(x))

print(tuple(map(lambda x:x*x, (1,2,3,4,5))))

#print('\n'.join(tuple(map(lambda a, p = int(input('Enter power: ')): f'{a} ^ {p} = {int(a) ** p}', input('Enter list of numbers: ').split()))))

#filter function
#filter fn filters the iterables based on condition 
#it accepts the fn and also the iterables as params.

def filterfn(x):
    if x>=3:
        return x

y = filter(filterfn, (1,2,3,4))
print(list(y))

y = filter(lambda x:(x>=3), (1,2,3,4))
print(list(y))


from functools import reduce


print(reduce(lambda a, b: a + b, filter(lambda x: 3 < x < 9, map(int, input('Enter numbers: ').split()))))
print('Sum:', reduce(lambda a, b: a + b, filter(lambda x: 3 < x < 9, map(int, input('Enter numbers: ').split()))))


from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def diet(self):
        pass

    @property
    def food_eaten(self):
        return self.__food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self.__food = food
        else:
            raise ValueError(f"This animal doesn't eat this food")


    @abstractmethod
    def feed(self):
        pass
 
    @abstractmethod
    def do(self, action):
        pass

class Lion(Animal):
    @property
    def diet(self):
        return ['antelope', 'cheetah', 'buffalo']
    def feed(self):
        print(f"Feeding a lion with {self.food_eaten}!")
    def do(self, action, time):
        print(f"{action} a lion at {time}")
class Panda(Animal):
    @property
    def diet(self):
        return ['bamboo', 'leaves']
    def feed(self):
        print(f"Feeding a panda with {self.food_eaten}!")
    def do(self, action, time):
        print(f"{action} a panda at {time}")

class Snake(Animal):
    @property
    def diet(self):
        return ['mice', 'rabbit']
    def feed(self):
        print(f"Feeding a snake with {self.food_eaten}!")
    def do(self, action, time):
        print(f"{action} a snake at {time}")

simba = Lion()
po = Panda()
cobra = Snake()

simba.food_eaten="buffalo"
simba.feed()
po.food_eaten='bamboo'
po.feed()
cobra.food_eaten='rice'
cobra.feed()


import os 
if os.path.exists("myfile.txt"):
    os.rename("myfile.txt", "myfilenew.txt")
    print("The file name has been renamed")
else:
    print("The file does not exist")


import os
from unittest import result
#creating a new directory
#os.mkdir("mkdir")
#print the current working directory
#print(os.getcwd())
#change the current working directory
#os.chdir("mkdir")
#print(os.getcwd())
#delete the directory that we created
#os.rmdir("mkdir")
#get the list of files and folders in a dir
#result = os.listdir(os.getcwd())
#print(result)


"""

#run an external python file(fileoutputsave.py)
#save its results as txt file

import subprocess
with open("myfile.txt", "wb") as f:
    subprocess.check_call()
