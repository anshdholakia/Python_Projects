#a=4
#b=24
#c=sum((a,b)) # this is a double bracket that is included in this syntax
#print(c)
def function1(a,b): # def means defined
    print("You are in function1", a+b)
#print(function1(5,12))
#function1(5,12) # none wont be printed
def func2(a,b):
    """This is a function that will calculate the average of two numbers- this is known as a doc-string"""
    average=(a+b)/2
    print("the average is", average)
    return average # it will store its value in v
#v=func2(5,12)
#print(v)
print(func2. __doc__) # this is used to access the doc string