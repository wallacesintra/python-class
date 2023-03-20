# Object Oriented Programming
# DEFINE CLASS Rectangle
        #  DECLARE length : real
#          DECLARE width : real
# DEFINE FUNCTION get(parameters: none) RETURNS VOID
#          prompt user for length
#          input length
#          prompt user for width
#          input width
#          CALL Area(Arguments: length,width)
# END FUNCTION
# DEFINE FUNCTION Area(parameters: l,w) RETURNS REAL
#          RETURN l*w
#END FUNCTION

# END CLASS

# START 
# DECLARE R = Rectangle()
# R.get()
# STOP

# Abstraction -
# encapsulation - burdling data + operations
#    -- private, - public

# program that uses the class rectangle whose data members are length and width and member methods are get and area
# all members are encapsulated and only accessed using class object

# class Rectangle:
#     def get(self):
#         self.length = int(input("enter the length: "))
#         self.width = int(input("enter the width: "))
#         A = self.Area(self.length,self.width)
#         print("the area is ",A)
#     def Area(obj,l,w):
#         obj.l = l
#         obj.w = w
#         return obj.l * obj.w    
# rect1 = Rectangle()
# rect1.get()


# inheritance - create new class to extend functionalities of some existing class
#              class derivedClass(parentClass):
#                   pass
# types of inheritance : single, multilevels, multiple , hierarchical

# example part time employee is a class derived from employee class

class Employee:
    def get(self):
        self.name = str(input("enter your name: "))
        self.age = int(input("enter your age: "))
        print("{0},you will retire after {1} ".format(self.name,65-self.age))

class partTime(Employee): 
    pass
p = partTime()
p.get()        

# multilevel
class a:
    def show(self):
        print("hello")
class b(a): 
    def talk(obj):
        print("How are you")
class c(b):
    def sound(o):
        print("fine")

# multiple inheritance
class circle:
    pass
class rectangle:
    pass
class cylinder(circle,rectangle):
    pass





# Abstraction - reveal only necessary
from abc import *

class David (ABC):
    @abstractmethod
    def buildTemple(self):
        pass
class solomon(David):
    def buildTemple(self):
        return super().buildTemple()
    
#  polymorphism - exist in different forms
