class employee:
    #def =  METHOD
    def EmployeeDetails(self): #need not be self, but for convinience
        self.name = "Mathew" #create name attribute
        print("Name = ",self.name)

        age = 30    #without using self parameter
        print("Age= ",age)  #
        #since we didnt use self method, the lifespan of this attribute is only within the method i.e. EmployeeDetails


    def PrintEmployeeDetails(self):
        print("Printing another method")
        print("Name: ", self.name)
        print("Age: ",age)

Employee_one = employee()

Employee_one.EmployeeDetails() #Function call. Commonly used
#object.attribute

employee.EmployeeDetails(Employee_one) #Function call. Literal sense
#classname.attribute(object)

Employee_one.PrintEmployeeDetails() #call function
#error is thrown because AGE is not defined with self.