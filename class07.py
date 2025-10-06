''' Multi level Inheritance:
when one parent clas has multiple child classes and one of the child class has its own child class
it is called multi level inheritance.'''

class Car:
    color="black"  # class variable
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):  # Toyota class inherits from Car class
    def __init__(self, brand):
        self.brand = brand
       
class Fortuner(Toyota):
    def __init__(self, type):
        self.type= type

car1= Fortuner("Diesel")
car1.start()  #inherited class method