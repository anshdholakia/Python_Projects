# Write a Python program to get the name of the operating system (Platform independent),
# information of current operating system, current working directory,
# print files and directories in the current directory and raises error in the case
# of invalid or inaccessible file names and paths.
# import os
# import platform
# print("Operating System:",os.name)
# print("\nInformation of current operating system: ",platform.platform())
# print("\nCurrent Working Directory: ",os.getcwd())
# print("\nList of files and directories in the current directory:")
# print(os.listdir('.'))
# print("\nTest if a specified file exis or not:")
# try:
#    filename = 'abc.txt'
#    f = open(filename, 'r')
#    text = f.read()
#    f.close()
# except IOError:
#    print('Not accessed or problem in reading: ', filename)



# Write a Python program to list only directories, files and all directories, files in a specified path.
# import os
# print("Only directories:")
# print([name for name in os.listdir('.') if os.path.isdir(os.path.join('.',name))])
# print("\nOnly files:")
# print([name for name in os.listdir('.') if not os.path.isdir(os.path.join('.',name))])
# print("\nFor all directories and files:")
# print([name for name in os.listdir('.')])



# Write a Python program to scan a specified directory and identify the sub directories and files
# def func(path):
#     import os
#     for entry in os.scandir(path):
#         if entry.is_dir():
#             typ='dir'
#         elif entry.is_file():
#             typ = 'file'
#         elif entry.is_symlink():
#             typ = 'link'
#         else:
#             typ = 'unknown'
#         print(f"{entry.name} {typ}")
# print(func('.'))



# Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified pat
# import os
# print('Exist:', os.access('.', os.F_OK))
# print('Readable:', os.access('.', os.R_OK))
# print('Writable:', os.access('.', os.W_OK))
# print('Executable:', os.access('.', os.X_OK))



# Write a Python program to create a symbolic link and read it to decide the original file pointed by the link
# import os
# path =os.path.basename(__file__)
# print('Creating link {} -> {}'.format(path, "ansh.txt"))
# os.symlink("ansh.txt", path)
# stat_info = os.lstat(".")
# print('\nFile Permissions:', oct(stat_info.st_mode))
# print('\nPoints to:', os.readlink("."))
# #removes the file path
# os.unlink(".")



# Write a Python program to create a file and write some text and rename the file name
# import os
# f=open("ansh3.txt","a")
# g=f.write("Ansh is a good boy")
# with open('ansh3.txt',"r") as f:
#     print(repr(f.read()))
# os.rename('ansh3.txt','ansh4.txt')



# Write a Python program to find the parent’s process id, real user ID of the current process and change real user ID
# import os
# print("Parent’s process id:",os.getppid())
# uid = os.getuid()
# print("\nUser ID of the current process:", uid)                   # This is for linux os (posix)
# uid = 1400
# os.setuid(uid)
# print("\nUser ID changed")
# print("User ID of the current process:", os.getuid())



# Write a Python program to retrieve the current working directory and change the dir (moving up one)
# import os
# print('Current dir:', os.getcwd())
# print('\nChange the dir (moving up one):', os.pardir)
# os.chdir(os.pardir)
# print('Current dir:', os.getcwd())
# print('\nChange the dir (moving up one):', os.pardir)
# os.chdir(os.pardir)
# print('Current dir:', os.getcwd())



# Write a python program to access environment variables and value of the environment variable
# print(os.environ)
# print("Access environ variable key:",os.getenv('JAVA_HOME'))



# Write a Python program to join one or more path components together and split a given path in directory and file
# import os
# path=r"."
# print(path)
# print("dir and file name:")
# print(os.path.split(path))
# print("join on eor more path components:")
# print(os.path.join(path,'a.txt'))



# Write a Python program to alter the owner and the group id of a specified file.
# import os
# fd = os.open( "ansh.txt", os.O_RDONLY )
# os.fchown( fd, 100, -1)
# os.fchown( fd, -1, 50)                              # only for linux(posix)
# print("Changed ownership successfully..")
# os.close( fd )




#Write a Python program to get information about the file pertaining to the file mode.
# Print the information - ID of device containing file, inode number, protection, number of hard links,
# user ID of owner, group ID of owner, total size (in bytes), time of last access,
# time of last modification and time of last status change.

# import os
# path = 'ansh.txt'
# fd = os.open(path, os.O_RDWR)
# info = os.fstat(fd)
# print (f"ID of device containing file: {info.st_dev}")
# print (f"Inode number: {info.st_ino}")
# print (f"Protection: {info.st_mode}")
# print (f"Number of hard links: {info.st_nlink}")
# print (f"User ID of owner: {info.st_uid}")
# print (f"Group ID of owner: {info.st_gid}")
# print (f"Total size, in bytes: {info.st_size}")
# print (f"Time of last access: {info.st_atime}")
# print (f"Time of last modification: {info.st_mtime }")
# print (f"Time of last status change: {info.st_ctime }")
# os.close(fd)




# Write a Python program to write a string to a buffer and retrieve the value written, at the end discard buffer memory
# import io
# # Write a string to a buffer
# output = io.StringIO()
# output.write('Python Exercises, Practice, Solution')
# # Retrieve the value written
# print(output.getvalue())
# # Discard buffer memory
# output.close()




# Write a Python program to run an operating system command using the os module.
# import os
# if os.name=='nt':
#     command='dir'
# os.system(command)



# Write a Python program to start a new process replacing the current process
# import os
# import sys
# program = "python"
# arguments = ["hello.py"]
# print(os.execvp(program, (program,) + tuple(arguments)))
# print("Goodbye")



# epoch time on this system
# import time
# print("Epoch on this platform:")
# print(time.gmtime(0))
# print("\nTime in seconds since the epoch:")
# print(time.gmtime(36000))




# Write a Python program to get time values with components using local time and gmtime.
# import time
# def time_struct(s):
#    print(' tm_year :', s.tm_year)
#    print(' tm_mon :', s.tm_mon)
#    print(' tm_mday :', s.tm_mday)
#    print(' tm_hour :', s.tm_hour)
#    print(' tm_min :', s.tm_min)
#    print(' tm_sec :', s.tm_sec)
#    print(' tm_wday :', s.tm_wday)
#    print(' tm_yday :', s.tm_yday)
#    print(' tm_isdst:', s.tm_isdst)
# print('\nlocaltime:')
# time_struct(time.localtime())
# print('\ngmtime:')
# time_struct(time.gmtime())




# Write a Python program to get different time values with components timezone,
# timezone abbreviations, the offset of the local (non-DST) timezone, DST timezone and time of different timezones.
# import time
# import os
# def zone_info():
#    print('TZ   :', os.environ.get('TZ', '(not set)'))
#    print('Timezone abbreviations:', time.tzname)
#    print('Timezone : {} ({})'.format(
#        time.timezone, (time.timezone / 3600)))
#    print('DST timezone ', time.daylight)
#    print('Time :', time.strftime('%X %x %Z'),'\n')
# print('Default Zone:')
# zone_info()
# TIME_ZONES = [
#    'Pacific/Auckland',
#    'Europe/Berlin',
#    'America/Detroit',
#    'Singapore',
# ]
# for zone in TIME_ZONES:
#    os.environ['TZ'] = zone
#    time.tzset()
#    print(zone, ':')
#    zone_info()




# Write a Python program that can suspend execution of a given script a given number of seconds.
# import time
# for x in range(4):
#     time.sleep(3)
#     print('I slept for 3 secs')



# Write a Python program to convert a given time in seconds since the epoch to a string representing local time
# import time
# print(time.ctime())
# print(time.ctime(236543789))



# Write a Python program to print simple format of time,
# full names and the representation format and preferred date time format.
# import time
# print("\nSimple format of time:")
# s = time.strftime("%a, %d %b %Y %H:%M:%S + 1010", time.gmtime())
# print(s)
# print("\nFull names and the representation:")
# s = time.strftime("%A, %D %B %Y %H:%M:%S + 0000", time.gmtime())
# print( s)
# print("\nPreferred date time format:")
# s = time.strftime("%c")
# print(s)
# s = time.strftime("%x, %X, %y, %Y")
# print("Example 11:", s)




# Write a Python program that takes a given number of seconds and pass since epoch as an argument.
# Print structure time in local time
# import time
# result = time.localtime(0000)
# print("\nResult:", result)
# print("\nYear:", result.tm_year)



# Write a Python program that takes a tuple containing 9 elements corresponding
# to structure time as an argument and returns a string representing it.
# import time
# tup=(1,2,3,4,5,6,7,8,9)
# result=time.asctime(tup)
# print(result)



# Write a Python program to parse a string representing time and returns the structure time.
# import time
# time_string = "22 January, 2020"
# print("String representing time:",time_string)
# result = time.strptime(time_string, "%d %B, %Y")
# print(result)
# time_string = "30 Nov 00"
# print("\nString representing time:",time_string)
# result = time.strptime(time_string, "%d %b %y")
# print(result)
# time_string = '04/11/15 11:55:23'
# print("\nString representing time:",time_string)
# result = time.strptime(time_string, "%m/%d/%y %H:%M:%S")
# print(result)
# time_string = '12-11-2019'
# print("\nString representing time:",time_string)
# result = time.strptime(time_string, "%m-%d-%Y")
# print(result)
# time_string = '13::55::26'
# print("\nString representing time:",time_string)
# result = time.strptime(time_string, "%H::%M::%S")
# print(result)


