''' Question: Define an Employee class with attributes role, department & salary.
This class alos showDetails() method.

Create an Engineer class that inherits properties from Employee and has additional
attrubutes: name & age. '''

class Employee:
    def __init__(self, role, department, salary):
        self.role= role
        self.department= department
        self.salary= salary

    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name= name
        self.age= age
        super().__init__("Engineer", "IT", 90000)  #calling parent class constructor

emp1= Engineer("AYESHA", 19)
emp1.showDetails()