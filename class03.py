''' Four pillars of OOPs
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

Abstraction means Hiding the implementation details of a class and only showing the essential features 
to the user.'''
class Car:
    def __init__(self):
        self.acc= False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=False
        print("Car started..")

c1=Car()
c1.start()

'''Encapsulation:
Wrapping data and functions into a single unit (object).
 class01 code is an example of encapsulation.'''