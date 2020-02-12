#parent class / Base class
class Apple:

    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("Contact us here: ", self.contactWebsite)

#child class / Derived class
class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufacturDetails(self):
        print("was manufacturer in year {} by {}".format(self.yearOfManufacture, self.manufacturer))

macbook = MacBook()
macbook.manufacturDetails()
macbook.contactDetails()
