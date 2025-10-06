'''Question: Define a Circle class to create a circle with radius r using the constructor.
Define an Area () method of the class  which calculates the area of the circle.
Define a Perimeter() method of the class which allows you to calculates the perimeter of the circle.'''

class Circle:
    def __init__(self, radius):
        self.radius= radius

    def Area(self):
        return  3.14 * self.radius **2    #Area= πr²

    def Perimeter(self):
        return 2 * 3.14 * self.radius    #Perimeter= 2πr

c1= Circle(21)
print("Area of circle:", c1.Area())
print("Perimeter of circle:", c1.Perimeter())