from abc import ABC, abstractmethod
class Calculate(ABC):
    @abstractmethod
    def calculate(self):
        pass

    @property
    def n1(self):
        return self.__n1

    @property
    def n2(self):
        return self.__n2

    @property
    def ans(self):
        return self.__ans

    @n1.setter
    def n1(self, n1):
        self.__n1 = n1

    @n2.setter
    def n2(self, n2):
        self.__n2 = n2

    @ans.setter
    def ans(self, ans):
        self.__ans = ans

class CalcSum(Calculate):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        

    def calculate(self):
        self.ans = self.n1 + self.n2
        return self.ans

class CalcDiff(Calculate):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def calculate(self):
        self.ans = self.n1 - self.n2
        return self.ans

class CalcProd(Calculate):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def calculate(self):
        self.ans = self.n1 * self.n2
        return self.ans
class CalcQuo(Calculate):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def calculate(self):
        if self.n2 !=0:
            self.ans = self.n1 // self.n2
            return self.ans
        else:
            print("Divisor can't be 0")
    
opt = 0

while opt!=5:

    print("Calculator")
    print("1. Sum \n 2. Difference \n 3. Product \n 4. Quotient \n 5. Exit")
    opt = int(input("Enter your option:"))

    if opt ==  1:
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        c = CalcSum(n1, n2)
        c.calculate()
        print(c.ans)
    elif opt == 2:
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        c = CalcDiff(n1, n2)
        c.calculate()
        print(c.ans)
    elif opt == 3:
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        c = CalcProd(n1, n2)
        c.calculate()
        print(c.ans)
    elif opt == 4:
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        c = CalcQuo(n1, n2)
        c.calculate()
        print(c.ans)
    elif opt == 5:
        pass
    else:
        print("Incorrect option!")


"""
class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def add(self):
        return self.n1 + self.n2
    
    def multiply(self):
        return int(self.n1*self.n2)
    
    def divide(self):
        return int(self.n1%self.n2)

calculate1 = Calculator(3, 6)
print("Sum =", calculate1.add(), "Product =", calculate1.multiply(), "Remainder =", calculate1.divide())

"""