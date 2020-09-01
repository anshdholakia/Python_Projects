class Employee:
    no_of_leaves=15

    def __init__(self,name,salary,role):   # init function makes the class take argument
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):  # self is meant as the object on which the code is written
            return f"Name is {self.name}, Salary is {self.salary} Rs and role is {self.role}"

    @classmethod   #using class methods we can change a variable value in a function
    def change_leaves(cls, newleaves): # cls is a class which has an instance of an object, it takes class not self
        cls.no_of_leaves=newleaves


    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good "+string)



ansh=Employee("Ansh",25000000,"CEO")
lewis=Employee("Lewis",20030020,"2nd CEO")
shaw=Employee.from_str("Shaw-494939-3rd CEO")


# print(ansh.no_of_leaves)
shaw.printgood("ansh")


################### ENCAPSULATION #########################
# Def: Hide details is known as encapsulation