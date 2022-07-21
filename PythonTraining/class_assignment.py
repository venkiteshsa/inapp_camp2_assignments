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

