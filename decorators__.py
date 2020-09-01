# def func1():
#     print("Hi, this is Ansh Dholakia")
# func2=func1()
# print(func2)

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcret(1)
# print(a)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1                               #also can be written like this
def Who_is_Ansh():
    print("Ansh is a gentleman")

# Who_is_Ansh =dec1(Who_is_Ansh) #dec1 is used to print this function with the previous functions
Who_is_Ansh()