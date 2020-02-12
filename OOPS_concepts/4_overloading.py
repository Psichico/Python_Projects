class square:

    def __init__(self,side):
        self.side = side

    def __add__(square_one, square_two):
        return ((4* square_one.side) + (4 * square_two.side))
    
    pass

square_one = square(5)
square_two = square(10)

print("Sum of sides of both the squares = ", square_one + square_two)

#we overloaded the add method here.