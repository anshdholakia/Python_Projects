"""
iterable- Is an python object where __iter__() or __getitem__() method are defined, when runned it gives iterator
iterator-it is an object in which the __next__() is defined
iteration-it is the process to iterate

"""

# generator- they generate on the fly value

# def gen(n):
#     for i in range(n):
#         yield i
#
# g=gen(33013121)
# print(g)


#Factorial generator

a=int(input("Enter number:"))

def factorial_gen(n):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
        yield fact



factorial_gen(a)
for i in factorial_gen(a):
    print(i)