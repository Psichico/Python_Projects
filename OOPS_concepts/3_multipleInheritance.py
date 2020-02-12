#base class
class OperatingSystem:
    multitasking = True
    name = "MacOS"
#base class
class Apple:
    website = "www.apple.com"
    name = "Apple"
#child class.
class MacBook(OperatingSystem, Apple): #Order of base class matters.

    def __init__(self):
        if self.multitasking is True:
            print("Multi task system. Visit {}".format(self.website))
            print("Name: ",self.name)

macbook = MacBook()
#what is both base class have same attribute?
#Diamond shape problem.

