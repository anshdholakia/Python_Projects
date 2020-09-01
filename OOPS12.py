class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="I am an instance variable in class A"
        self.special="special"



class B(A):
    classvar1="I am class variable in class B"
    def __init__(self):                  # Will show an warning on init as the fucntion is overwriten
        super().__init__()               # super is written in code as to call the original init
        self.var1="I am inside class B's constructor"
        self.classvar1="I am an instance variable in class B"


a=A()
b=B()

print(b.special, b.var1, b.classvar1)  # this fucntion will search for instance varibles first and then class variables