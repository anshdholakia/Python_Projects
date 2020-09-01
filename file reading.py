# f = open("ansh2.txt", "a") # for creaitng a file as well as writing multiple lines
# a=f.write("Ansh is a good boy\n")
# print(a) # number if characters that are written will be printed
# f.close()

# f = open("ansh2.txt", "w") #for creating a new file and for writing A line
# f.write("Ansh is a good boy\n")
#  # number if characters that are written will be printed
# f.close()

# Handle read and write both
f = open("ansh2.txt","r+")
f.write("good boy only\n")

print(f.read())