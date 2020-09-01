# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.
# from array import *
# s=array('i',[1,3,5,7,9])
# for i in s:
#     print(i)
# print("Here are the first values:\n")
# print(s[0])
# print(s[1])
# print(s[2])




# Write a Python program to append a new item to the end of the array
# from array import *
# s=array('i',[1,2,3,4])
# s.append(5)
# print("Appending 5 to s:",s)




# Write a Python program to reverse the order of the items in the array
# from array import *
# s=array('i',[1,2,3,4])
# s.reverse()
# print("Reversed",s)




# Write a Python program to get the current memory address and the length in
# elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
# from array import *
# s=array('i',[1,2,3,4])
# v=s.buffer_info()
# for i in range(len(s)):
#     print(f"The size of {i} element is {v[1]} and address is {v[0]}")




# get number of occurences of a specific element
# from array import *
# s=array('i',[1,2,3,4,3])
# print(s.count(3))




# Write a Python program to append items from inerrable to the end of the array
# from array import *
# s=array('i',[1,2,3,4])
# s.extend(s)
# print(s)




# convert bytes to string
# from array import *
# s=array('b',[99,100,101,102,103,104])
# x=s.tobytes()
# print(x)




# Write a Python program to append items from a specified list.
# from array import *
# s=array('i',[1,2,3,4])
# lis=[5,6,7]
# s.fromlist(lis)
# print(s)




# Write a Python program to insert a new item before the second element in an existing array
# from array import *
# s = array('i', [1, 2, 3, 4])
# s.insert(1,3)
# print(s)




# Write a Python program to remove a specified item using the index from an array
# from array import *
# s=array('i',[1,2,3,4,5])
# s.remove(2)
# print(s)



# Write a Python program to remove the first occurrence of a specified element from an array
# from array import *
# s=array('i',[1,2,3,4,5,1])
# s.remove(1)  # it will remove 1's first occurence
# print(s)




# Write a Python program to convert an array to an ordinary list with the same items.
# from array import *
# s=array('i',[1,2,3,4])
# x=s.tolist()
# print(x)




# Write a Python program to find whether a given array of integers contains any duplicate element.
# Return true if any value appears at least twice in the said array and return false if every element is distinct.
# from array import *
# s=array('i',[1,2,3,4,1])
# for i in s:
#     if s.count(i)>1:
#         print(True)
#         exit()
# print(False)




# Write a Python program to find the first duplicate element in a given array of integers.
# Return -1 If there are no such elements.
# from array import *
# s=array('i',[1,2,3,4,1])
# for i in s:
#     if s.count(i)>1:
#         print(i)
#         exit()
# print(-1)
