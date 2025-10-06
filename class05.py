class Account:
    def __init__(self, acc_no, ascc_pass):
        self.acc_no= acc_no
        self.__acc_pass= ascc_pass  #private attribute, use __ before attribute name.

    def get_pass(self):
        return self.__acc_pass

acc1= Account(12345, "abc@123")
print(acc1.acc_no)
print(acc1.get_pass())  #accessing private attribute using getter method

class Person:
    def __hello(self):   #private method
        print("Hello Students!")

    def welcome(self):
        self.__hello()

p1= Person()
p1.welcome()  #accessing private method using public method