class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gamil.com"

    def explain(self):
        return f" This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname== None:
            return ("Email is not set")
        return f"{self.fname}.{self.lname}@gamil.com"  #To print hiro after changing fname that was Ansh, Setters are used.


    @email.setter # How to set that when an email is typed, the fname and lname change automatically with respect to the email
    def email(self,string):
        print("Setting now...")
        names=string.split("@")[0]
        self.fname=names.string.split(".")[0]
        self.lname=names.string.split(".")[1]


    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None




Ansh= Employee("Ansh","Dholakia")

Lewis= Employee("Harry","Lewis")

print(Ansh.email)

Ansh.fname="Hiro"

# print(Ansh.email)  #  * It wont print Hiro instead of Ansh as the email is already initialised when made an object

# print(Ansh.fname)

del Ansh.email
print(Ansh.email)