f=open("ansh.txt")
print(f.tell()) # this funtion tells me where my pointer is on which character
print(f.readline())
# print(f.tell())
f.seek(0) # it resets the pointer to character 0 hence it will read the same line as pointer is at 0 char
print(f.readline())