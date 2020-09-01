import os

# print(dir(os))
# print(os.getcwd()) #getcwd= get current working directory
# os.chdir("C://") #changing directory
# print(os.getcwd())
# f=open("ansh.txt")  # error a s it is not present in C:// directory
# print(os.listdir("C://"))

# os.mkdir("ansh")  #creates a direcotory/file called ansh

# os.makedirs("this/that") #It creates a file this and that file inside this file

# os.rename("ansh.txt","harry.txt") #It changes ansh.txt to harry.txt

# print(os.environ.get('Path')) #It will find path from environment variables

# print(os.path.join("C://", "ansh.txt"))

print(os.path.exists('C://Program Fvles')) #tells if path exists or not

print(os.path.isfile('C://Program Files')) #tells if it is a file or not