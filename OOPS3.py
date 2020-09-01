class Employee:
    no_of_leaves=15

    def __init__(self,name,salary,role):   # init function makes the class take argument
        self.name=name
        self.salary=salary
        self.role=role

        def printdetails(self):  # self is meant as the object on which the code is written
            return f"Name is {self.name}, Salary is {self.salary} Rs and role is {self.role}"

ansh=Employee("Ansh",25000000,"CEO")
# lewis=Employee()

# ansh.name="Ansh"
# ansh.salary=25000000
# ansh.role="CEO"
#
# lewis.name="Lewis"
# lewis.salary=223343434
# lewis.role="2nd CEO"
#
# print(lewis.printdetails())

print(ansh.salary)