class Employee:
    no_of_leaves=15

    def __init__(self,name,salary,role):   # init function makes the class take argument
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):  # self is meant as the object on which the code is written
            return f"Name is {self.name}, Salary is {self.salary} Rs and role is {self.role}"

    @classmethod   #using class methods we can change a variable value in a function
    def change_leaves(cls, newleaves):
        # cls is a class which has an instance of an object, it takes class not self
        cls.no_of_leaves=newleaves




    def __add__(self, other): ####   Using this function we can Dunder add, emp1 and emp2
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return self.printdetails()




emp1=Employee("Ansh",233,"CEO")
emp2=Employee("Lewis",233,"CEO 2nd")

print(emp1) #using add functions we have Dunder added emp1 and emp2

