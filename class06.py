''' Inheritance:
When one class ( child) derives the properties and methods of another class ( parent) 
it is called inheritance.
1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
this code is the example of single inheritance'''

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
        print(f"Car brand is {self.brand}")  # accessing parent class method

t1= Toyota("Innova")
t1.start()  #inherited class method
print(f"Car's color is {t1.color}")  #inherited class variable 