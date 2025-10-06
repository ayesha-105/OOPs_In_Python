#creating class
class Student:
    university_name="SMIU" #class attribute
#default constructor
    def __init__(self):
        pass

#parameterized constructor
    def __init__(self, name, marks):  
        self.name= name                   #instance attribute
        self.marks= marks
        print("Adding new student in database..") 
#instance method
    def welcome(self):
        print("Welcome to ", self.university_name, self.name)
#get method returns the value of marks
    def get_marks(self):
        return self.marks


#creating object (instance)
s1= Student("Ayesha Malik", 92)
s1.welcome()
print(s1.get_marks())
print(s1.university_name)

#if class and obj attr has same same name, obj attr will be given preference becuase obj attr > class attr