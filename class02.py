#Static Methods
class Student:
    @staticmethod            #This is decorator, It changes the behaviour of method
    def hello():
        print("Hello Students!")
s1= Student()
s1.hello()  #calling static method using object