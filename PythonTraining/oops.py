"""
# Class
class Employee:
    'Common base class for all employees'
    empCount = 0

    #constructor
    #self is an instance of the class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1 #increment employee count when new object is created

    def displayEmpCount(self):
        print("Total no. of employee:", Employee.empCount)
    
    def displayEmployeeDetails(self):
        print("Name:", self.name, "Salary:", self.salary)

    
employee1 = Employee("Tom", 2000)
employee1.displayEmployeeDetails()
employee1.displayEmpCount()

employee2 = Employee("Jerry", 3000)
employee2.displayEmployeeDetails()
employee2.displayEmpCount()

#not recommended
print("Total Employee count", Employee.empCount)


#Inheritence and Encapsulation

#creating main class
class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" %(self.name, self.distance)

#creating sub class
class MarsRover(Rocket):
    def __init__(self, name, distance, maker, __vehiclecode):
        Rocket.__init__(self, name, distance)
        self.maker = maker
        self.__vehiclecode = __vehiclecode
    
    def get_maker(self):
        return "%s launched by %s" %(self.name, self.maker)
    
    def getVehicleCode(self):
        return self.__vehiclecode

x = Rocket("simple rocket", "till stratosphere")
y = MarsRover("mars_rover", "till Mars", "ISRO", "1234")

print(x.launch())
print(y.launch())
print(y.get_maker())
#to access private variable
print(y.getVehicleCode())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def display(self):
        print(self.name)
        print(self.__age)
    
person = Person('Dev', 30)
#accessing using class method
person.display()

#accessing directly from outside without any issues
print(person.name)
#__age is private
#print(person.__age)
print(person._Person__age)



#Polymorphism

from math import pi
from mimetypes import init

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape"
    
    #represents the class objects as a string
    def __str__(self):
        return self.name
    
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    
    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees"
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return pi*self.radius**2

a = Square(6)
b = Circle(5)

print(b)
print(b.fact())
print(b.area())
print(a)
print(a.fact())
print(a.area())




class Hero:

    @classmethod
    def sayClassHello(cls): #since its classmethod, will receive class ref as implicit
        if cls.__name__ == "HeroSon":
            print("Hello Prince")
        elif cls.__name__ == "HeroDaughter":
            print("Hello Princess")
    
    @staticmethod
    def sayHello():
        print("Hello")
    
class HeroSon(Hero):
    def saySonHello(self): #first impl arg will be self since its a regular method
        print("Hello Son")
    
class HeroDaughter(Hero): #first impl arg will be self since its a regular method
    def sayHelloDaughter(self):
        print("Hello Daughter")
    
testson = HeroSon()
testson.sayClassHello()
testson.saySonHello()
testson.sayHello()

testdaughter = HeroDaughter()
testdaughter.sayClassHello()
testdaughter.sayHelloDaughter()
testdaughter.sayHello()


"""

class House:
    #constructor
    def __init__(self, price):
        self.__price = price #keeping the price as private __price
    
    #creating the getter method for fetching the attribute value in a class
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    @price.deleter
    def price(self):
        del self.__price


#typical access and update will be like this:
house = House(500000) #create obj
print(house.price) #access attributes
house.price = 100000 #modifying the attribute
print(house.price) #access attributes
del house.price #delete price of the house instance
print(house.price)
