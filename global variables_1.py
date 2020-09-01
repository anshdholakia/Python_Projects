# l=10 # this is a global variable and has a global scope
# def func1(k):
#     print("You entered",k)
#     global l
#     l=l+12 #local variable cannot change global variable without using global l function
#     l=22
#     print(l) # l will print 22 as l is defined INSIDE the function, so the global variable only inside the function gets changed
#
# func1(2)
# print(l) # l is not 22 as its is 10 as a global variable hence l will always be 10

def ansh():
    x=2 #this is not a global variable, a globla variable is out of the nest.
    def rohan():
        global x #this wont change the value as x is not global but local of the nested function
        x=22
    print("The value before calling rohan() is",x)
    rohan()
    print("The value before calling rohan() is",x)
ansh()