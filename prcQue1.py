'''Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
'''
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"Hi!{self.name}, Your average score is {sum/3}")

s1= Student("Ayesha Malik", [92, 85, 78])
s1.get_avg()
