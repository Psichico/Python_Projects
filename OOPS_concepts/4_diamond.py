class A:
    def method(self):
        print("Belongs to class A")
    pass

class B(A):
    def method(self):
        print("Belongs to class B")
    pass

class C(A):
    def method(self):
        print("Belongs to class C")
    pass

#Method resolution order. B or C, what to choose.
class D(B, C): #order of class is the priority. 
    
    pass

d_object = D()
d_object.method()
