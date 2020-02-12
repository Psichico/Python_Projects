from abc import ABCMeta, abstractmethod

class shape(metaclass = ABCMeta):
     ###Abstract base class 
    @abstractmethod
    def area(self):
        return 0


class square(shape):

    side = 4

    def area(self):
        print("Area of square: ",self.side * self.side)


class rectangle(shape):

    width = 5
    length = 10

    def area(self):
        print("area of rectangle = ", self.width * self.length)

sq = square()
re = rectangle()
sq.area()
re.area()
