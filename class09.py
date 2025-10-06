class Car:
    def __init__(self, type):
        self.type= type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)

car1= Toyota("Innova", "electric")
print(car1.brand)
print(car1.type)