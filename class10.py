''' Claas Method:
A class method is a method that is bound to the class and not the object of the class.
'''
class Person:
    name= "Ayesha Malik"

    # def change_name(self, name):
    #     self.__class__.name= name  #accessing class variable using class name

    @classmethod
    def change_name(cls, name):
        cls.name= name
p1= Person()
p1.change_name("Areeba")
print(Person.name)