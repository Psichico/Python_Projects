#What are instance methods.
#They are the methods of your class that make use of the self param to access and modify the instance attributes of class.

class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod #decorators. starts with @
    def welcomeMessage():
        print("WELCOME") #we are declaring self, but nowhere in the body we are using the self param.
                         #what is the usefulness? 


employee_one = Employee()
employee_one.employeeDetails()
print(employee_one.name)

employee_one.welcomeMessage()
