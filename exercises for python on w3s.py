# t=(input("when will your exam start:\n"))
# split=t.split(",") #split[1]
# split1=split[0].split("(") #split1[1]
# split2=split[2].split(")") #split2[0]
# print(split1[1],"/",split[1],"/",split2[0]
#
# from datetime import date
#
# a=input("Enter a date1:")
# b=input("Enter a date2:")
# split=a.split(",") #split[1]
# split1=split[0].split("(") #split1[1]
# split2=split[2].split(")") #split2[0]
# split2[0]=int(split2[0])
# split[1]=int(split[1])
# split1[1]=int(split1[1])
# c=date(split2[0],split[1],split1[1])
#
# split3=b.split(",") #split3[1]
# split4=split3[0].split("(") #split4[1]
# split5=(split3[2].split(")")) #split5[0]
# split5[0]=int(split5[0])
# split3[1]=int(split3[1])
# split4[1]=int(split4[1])
#
# d=date(split5[0],split3[1],split4[1])
#
#
#
# diff=d-c
# print(diff.days)
#
# a=input("Enter a sentence:\n")
# if a.startswith("is"):print(a)
# else:print(f"is {a}")

# a=input("Enter a word:\n")
# b=a.split()
# while i> len(a):
#     if b[i] in ["i","a","e","o","u"]:
#         print("True")
#     i+=1
# list=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527]
#
# for i in range(0, len(list)):
#     if list[i]%2==0 and list[i]<237:
#         print(list[i])
#     elif list[i]>237:
#         continue
#     else:
#         continue



#                  VERY IMP - LCM EXERCISE

# def lcm(x, y):
#    if x > y:
#        z = x
#    else:
#        z = y
#
#    while(True):
#        if((z % x == 0) and (z % y == 0)):
#            lcm = z
#            break
#        z += 1
#
#    return lcm
# a=int(input("Enter the first number:\n"))
# b=int(input("Enter the second number:\n"))
# print("The lcm is:",lcm(a,b))




# x=int(input("Enter a number:\n"))
# y=int(input("Enter the second number:\n"))
#
# print(f"The result  ({x}+{y})^2 is:", (x + y) * (x + y))



# to determine if python is 32 or 64 bit:
#
# import struct
# print(struct.calcsize("P")*8)

#to determine which file is currently executing:
# import os
# print(os.path.realpath(__file__))

#to determine the number of CPUs used
# import multiprocessing
# print(multiprocessing.cpu_count())


#to list all files in a directory
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('Users\Ansh\PycharmProjects\First Project File') if isfile(join('Users\Ansh\PycharmProjects\First Project File', f))]
# print(files_list)


#how to access environment variables
# import os
# # Access all environment variables
# print('*----------------------------------*')
# print(os.environ)
# print('*----------------------------------*')
# # Access a particular environment variable
# print(os.environ['TEMP'])
# print('*----------------------------------*')
# print(os.environ['Path'])
# print('*----------------------------------*')


# how to acccess username

# import getpass
# print(getpass.getuser())

#finding IP address
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# finding height and width of console
# def terminal_size():
#     from importlib import reload
#     import termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th
#
# print('Number of columns and Rows: ',terminal_size())

#To sort files by date

# import glob
# import os
#
# files = glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))


#to print files date and time wise
# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time
#
# # Relative or absolute path to the directory
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#
# # all entries in the directory w/ stats
# data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path), path) for path in data)
#
# # regular files, insert creation date
# data = ((stat[ST_CTIME], path)
#         for stat, path in data if S_ISREG(stat[ST_MODE]))
#
# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path))


# get math module details
# import math
# print(dir(math))

# to check whether platform is big end or little end
# import sys
#
# if sys.byteorder == "little":
#     #intel, alpha
#     print("Little-endian platform.")
# else:
#     #motorola, sparc
#     print("Big-endian platform.")

# to check modules in python
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))

# to check whether all elements in a list are smaller than a particular number
# ls=[1,2,3,3,4,5,6,7,7,5,7,5,554,6,5,654,433]
# print(all(x>-22 for x in ls))

# test the number of occurence of a specific character
# a=input("Enter a string:\n")
# print(a.count("a"))

# to get ASCII value
# print(ord("e"))


# to check if string is numeric
# a=input("Enter a numeric string")
# if a.isnumeric():
#     print("Yes, it is numeric")
# else:
#     print("It is not numeric")

# to print stack
# import traceback
# def abc():
#     return a()
# def a():
#     traceback.print_stack()
# abc()



#getting system time
# import time
# print(time.ctime())


# to clear system or terminal
# import os
# import time
# # for windows
# # os.system('cls')
# os.system("windows")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')


# server name
# import socket
# host_name = socket.gethostname()
# print()
# print("Host name:", host_name)
# print()

#to get users environment
# import os
# print(os.environ)


#to retrieve file properties
# import os.path
# import time
#
# print('File:', __file__)
# print('Access time:', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time:', time.ctime(os.path.getctime(__file__)))
# print('Size:', os.path.getsize(__file__))

#computing product of numbers in a list without for loop
# from functools import reduce
# nums = [10, 20, 30,23,123,12,1,2,2,2,42]
# nums_product = reduce( (lambda x, y: x * y), nums)
# print("Product of the numbers : ",nums_product)


# to check if lowercase letters are present in the string or not
# a=input("Enter a string:\n")
# if a.islower()==True:
#     print("The string has lowercase letters")
# else:
#     print("The string does not have lowercase letters")



# how to list home directory without absolute directory
# import os
# print(os.path.expanduser("~"))


# write the number without spaces
# import re
# str='''
# asdf=23143'''
#
# it=str.split("=")
# patt=re.findall(r'=\S+',str)
# print(f"Value of {it[0]} is{patt[0]}

# to check if ip address is correct or not
# import socket
# add="1.23.1.3"
# try:
#     socket.inet_aton(add)
#     print("Correct IP address")
# except socket.errors:
#     print("Invalid address")

