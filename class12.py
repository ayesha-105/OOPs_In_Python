''' Polymorphism:
    - Poly means many - Morph means forms  , so polymorphism means many forms.
    We use overloading and overriding. Overloading operator means same operator is used for different purpose.
    Overriding means same method name is used in parent and child class with different implementation.'''

class Complex:
    def __init__(self, real, imag):
        self.real= real
        self.imag= imag

    def showingNumber(self):
        print(f"The complex number is: {self.real}i + {self.imag}j")

    def __add__(self, num2):           #dunder function for operator overloading
        Real= self.real + num2.real
        Imag= self.imag + num2.imag
        return Complex(Real, Imag)
    
    def __sub__(self, num2):           
        Real= self.real - num2.real
        Imag= self.imag - num2.imag
        return Complex(Real, Imag)

num1= Complex(3, 4)
num1.showingNumber()


num2= Complex(1, 3)
num2.showingNumber()

#num3 = num1.add(num2)
num3= num1 + num2  #operator overloading
num3.showingNumber()

num3= num1 - num2
num3.showingNumber()