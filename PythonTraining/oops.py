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
