# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
# print([i for i in range(1500,2701) if i%7==0 and i%5==0])



# Write a Python program to guess a number between 1 to 9
# import random
# d=random.randrange(1,10)
# a=int(input("Enter your guess:\n"))
# while(d!=a):
#     a=int(input("Enter your guess:\n"))
# print(f'Correct guess:{a}')



# Write a Python program to construct the following pattern, using a nested for loop
# a=int(input("Enter the number of rows(odd):\n"))
# for i in range(0,a):
#     if(i<a/2):
#         for j in range(0,i+1):
#             print("* ",end="")
#         print("\n",end="")
#     else:
#         for j in range(0,a-i):
#             print("* ",end="")
#         print("\n",end="")




# Write a Python program to get the Fibonacci series between 0 to 50.
# sum=0
# i=1
# while(sum<50):
#     print(sum)
#     sum,i=i,i+sum



# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# row=int(input("Enter the number rows:\n"))
# col=int(input("Enter the number coloumns:\n"))
# lis=[[0 for cols in range(col)] for rows in range(row)]
# for i in range(row):
#     for j in range(col):
#         lis[i][j]=i*j
#
# print(lis)





# Write a Python program to construct the following pattern, using a nested loop number
# for i in range(1,10):
#     for j in range(0,i):
#         print("%d"%i,end="")
#     print("\n",end="")


