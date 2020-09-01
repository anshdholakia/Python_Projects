# Write a Python program to read an entire text file
# with open("ansh.txt","r") as f:
#     r=f.read()
#     print(r)


# Write a Python program to read first n lines of a file
# n=int(input("Enter the number of lines: "))
# with open("ansh.txt","r") as f:
#     for i in range(0,n):
#         d=f.readline()
#         print(d,end="")


# Write a Python program to append text to a file and display the text.
# with open('ansh.txt','a') as f:
#     f.write("Ansh is driving the robotics revolution")
#     txt=open("ansh.txt")
#     print(txt.read())


# Write a Python program to read last n lines of a file
# a=int(input("Enter the last n lines: "))
# with open("ansh.txt","r") as f:
#     r=f.readlines()
#     for i in range(1,a+1):
#         print(r[-i])


# Write a Python program to read a file line by line and store it into a list
# with open("ansh.txt","r") as f:
#     w=f.readlines()
#     print(w)


# Write a Python program to read a file line by line store it into a variable
# with open("ansh.txt","r") as f:
#     w=f.readlines()
#     for i in range(0,len(w)):
#         a=w[i]
#         print("Value of a:",a)

# Write a Python program to count the frequency of words in a file.
# from collections import Counter
# with open("ansh.txt") as f:
#     print(Counter(f.read().split()))


# Write a Python program to get the file size of a plain file
# import os
# info=os.stat("ansh.txt")
# print(info.__sizeof__())


# Write a Python program to write a list to a file
# lis=[1,2,4,5]
# f=open("ansh.txt","a")
# w=f.write(str(lis))
# f.close()


# Write a Python program to copy the contents of a file to another file
# f=open("ansh.txt","r").read()
# w=open("ansh2.txt","w")
# d=w.write(f)


# to check if file is closed or not
# f=open("ansh.txt","r")
# print(f.closed)
