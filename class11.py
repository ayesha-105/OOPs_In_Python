'''@property decorator:
    - used to define a method as a property'''

class student:
    def __init__(self, maths, phys, eng):
        self.maths= maths
        self.phys= phys
        self.eng= eng
       
    # def calcpercentage(self):
    #      self.percentage=(f"{(self.maths + self.phys + self.eng)/3}%")

    @property
    def percentage(Self):
        return (f"{(Self.maths + Self.phys + Self.eng)/3}%")

s1= student(90, 80, 70)
print(s1.percentage)

s1.phys= 85
print(s1.percentage)
