class Employee:
    var=8
    no_of_leaves=15   # this is public variable
    _protected=1      # this is protected variable
    __private=22      # this is private variable

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



class Player:
    var=9
    no_of_games=12
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} Rs and role is {self.role}"

class CoolEmployee(Player, Employee):
    # var=10
    language="C#"
    def printlanguage(self):
        print(self.language)



emp=Employee("Ansh",2948,"CEo")
print(emp._protected)  # this will print as it is protected
print(emp._Employee__private)  # as it is private, have to add _class name in front