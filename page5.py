#classes
# Multiple classes can be placed in a single file.  Classes are placed in multiple files if code becomes very big and need to put the critical parts of the code into multiple files, to make it easily accessible by other team programmers.

# Can multiple object be created from the same class?
# Yes, multiple objects can be created

# Can objects create classes?
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myGreeting(self):
    print("Hello my name is " + self.name)

# use setter and getter to implement data hiding
p1 = Person("Jake", 36)
p1.myGreeting()

# Module ------------------------------------------

import math  
    
a = math.pi / 6
     
# returning the value of sine of pi / 6  
print ("The value of sine of pi / 6 is : ", end ="")  
print (math.sin(a))  

# multiple inheritance

class Class1: 
    def m(self): 
        print("Called function in Class1")  
        
class Class2(Class1): 
    def m(self): 
        print("Called function in Class2") 
  
class Class3(Class1): 
    def m(self): 
         print("Called function in Class3")      
      
class Class4(Class2, Class3): 
    def m(self): 
        print("Called function in Class4")    
  
obj = Class4() 
obj.m() 
  
Class2.m(obj) 
Class3.m(obj) 
Class1.m(obj) 

# A static method
# called without an object but cannot be utilized in collections

class C:
    @staticmethod
    def f(arg1, arg2):
        print("The values are", arg1, arg2)

C.f(3,4)  

# iterable data type can be lists, tuples, dictionaries and sets

mytuple = ("toyota", "nissan", "honda")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# With class method

class MyClass:

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

print(MyClass.classmethod())
print(MyClass.staticmethod())
