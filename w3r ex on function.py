# Write a Python function to multiply all the numbers in a list.
# def func(lis):
#     a=1
#     for i in range(len(lis)):
#         a*=lis[i]
#     return a
# print(func([8, 2, 3, -1, 7]))




# Write a Python program to reverse a string.
# def func(stra):
#     return stra[::-1]
# print(func('1234abcd'))



# Write a Python function that prints out the first n rows of Pascal's triangle
# def func(rows):
#     trow=[1]
#     y=[0]
#     for x in range(max(rows,0)):
#         print(trow)
#         trow=[l+r for l,r in zip(trow+y,y+trow)]
#     return rows>=1
# print(func(9))



# Write a Python function to check whether a string is a pangram or not
# def func(stra):
#     import string
#     b=set(string.ascii_lowercase)
#     lis=[]
#     for i in stra:
#         lis.append(i)
#     return set(lis).intersection(b)==b
# print(func("The quick brown fox jumps over the lay dog"))



# Write a Python program to detect the number of local variables declared in a function.
# def func(n):
#     n=2
#     x=3
#     return n+x
# print(func.__code__.co_nlocals)
