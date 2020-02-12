class MusicalInstruments:

    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):

    typeOfWood = "Tonewood"

class Guitar(StringInstruments):

    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. Made of {} and can play {}".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))

guitar = Guitar()