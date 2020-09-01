# # printing patterns
# f=open("ansh.txt")
# j=open("ansh2.txt")
# con=j.read()
# content=f.read()
# inint=int(input("Enter any number\n"))
# inbo=int(input("Enter 0 or 1\n"))
#
# while (True):
#
#     if inint & inbo == True:
#         print(content)
#         break
#
#
#     elif inint & inbo == False:
#         print(con)
#         break
#
#     else:
#         print("Invalid input\n")
#         exit()
#

print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()

