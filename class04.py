#del keyword is used to delete the object
class Student:
    def __init__(self, name):
        self.name= name

s1= Student("Ayesha Malik")
print(s1.name)

del s1
print(s1.name)  #this will give error because object is deleted 