#check if employee has achieved his weekly target or not

class employee:
    name = "Ben"
    designation = "Sales Executive"
    SalesMadeThisWeek = 6
    def HasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target achieved")
        else:
            print("Target not achieved")


#create object

EmployeeOne = employee()
print(EmployeeOne.name)

#Above methods are not well. If you create another object, it will have same attributes as object 1.
#Hence there is another way to write class and object

numbers = [1, 2, 3]
numbers.append(4)
print(type(numbers))
print (numbers)
print("\n")
print("\n")
