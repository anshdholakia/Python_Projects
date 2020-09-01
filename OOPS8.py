class Employee:
    var=8
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




ansh=Employee("Ansh",25000000,"CEO")
lewis=Employee("Lewis",20030020,"2nd CEO")

# vikk=CoolEmployee("vikk",3000202020220,"Gamer")
# vikk.printlanguage()
# det=vikk.printdetails()
# print(det)

vikk=CoolEmployee("vikk",["Football"])  # As vikk has two arguments it will go to the player class and print the var there
print(vikk.var)

Shaw=Player("Shaw",["Football"])
