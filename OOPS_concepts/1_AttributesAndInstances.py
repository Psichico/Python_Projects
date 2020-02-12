## Attributes (class and instance) and Methods (static and instance)
## self parameter, init.

class employee:
    NumberOfWorkingHours = 40

employeeOne = employee()
employeeTwo = employee()

#access and change the class attribute
employee.NumberOfWorkingHours = 45

#class attribute is common to all instances of class
#instance attribute is specific to each attribute of class

employeeOne.name = "John" #instance attribute
employeeTwo.name = "Mary" #instance attribute

employeeOne.NumberOfWorkingHours = 40 #only 40 for this instance
#when we use name of object class attribute, we create an instance attribute and assign value to it.

employeeTwo.NumberOfWorkingHours
#This will first check if there is an instance attribute, if not it will check for the class attribute and assign value accordingly

employeeOne.age
#This will check if there is an instance attribute, if not, it will check if there is a class attribute. If not, it will throw an error



