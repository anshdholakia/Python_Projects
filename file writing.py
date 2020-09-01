f=open("ansh.txt", "r") # f becomes a file pointer as open function returns a file pointer
print(f.readline())
print(f.readline())
print(f.readline())
# f=open("ansh.txt", "rb") # it is in binary form \r\ form
# f=open("ansh.txt", "rt") # it is default mode that will give a text file
#content=f.read()
#print(content)
# for line in f:
#     print(line, end="")  # how for function is used
# content=f.read(20332)
# print("1", content)

# #content=f.read(3) # it will read 3 characters
# content=f.read(20332) # this statement will be ignored as the first one is taken into account only
# print("2", content)
f.close() #it is a good practice to do this