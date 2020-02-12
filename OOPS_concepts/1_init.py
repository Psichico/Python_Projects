#

class Employee:

    #only in python
    #init method is invoked by default when an object is created
    def __init__(self, name):
        self.name = name #requires parameter when object is created

#    def enterEmployeeDetails(self):
#        self.name = "Mark"

    def displayEmployeeDetails(self):
        print(self.name)

employee_one = Employee("Mark")

employee_one.displayEmployeeDetails() #call second method without calling first method
#Problem: Initialization happens in first method, hence we need a method to initialize all the attributes.

employee_two = Employee("Mathew")
employee_two.displayEmployeeDetails()

