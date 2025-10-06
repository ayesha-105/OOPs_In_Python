''' Multiple Inheritance:
When a class (child) derives the properties and methods of more than one class (parent)
it is called multiple inheritance.'''

class A:
    varA= "Welcome to class A"

class B:
    varB= "Welcome to class B"

class C(A, B):  # C class inherits from A and B class
    varC= "Welcome to class C"

c1= C()
print(c1.varA)  # inherited class variable from class A
print(c1.varB)  # inherited class variable from class B
print(c1.varC)  # inherited class variable from class C