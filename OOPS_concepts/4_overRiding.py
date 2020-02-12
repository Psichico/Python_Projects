class Employee:

    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.NumberOfWorkingHours)

class Trainee(Employee):

    #overriding the base class method
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()

print("Number of working hours: ", end = ' ')
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours TRAINEE: ", end = ' ')
trainee.displayNumberOfWorkingHours()

##What if we want to call NumberOfWorking hours from base class??
## use SUPER function

trainee.resetNumberOfWorkingHours()
print("Number of working hours TRAINEE: ", end = ' ')
trainee.displayNumberOfWorkingHours()