# Write a Python program to convert an integer to a roman numeral
# class roman:
#     def int_to_roman(self,num):
#         val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#         syb=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
#         roman_num=''
#         i=0
#         while num>0:
#             for _ in range(num // val[i]):
#                 roman_num+=syb[i]
#                 num-=val[i]
#             i+=1
#         return roman_num
# print(roman().int_to_roman(1))
# print(roman().int_to_roman(4000))



# Write a Python class to get all possible unique subsets from a set of distinct integers
# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))
#
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]
#
#
# print(py_solution().sub_sets([4, 5, 6]))



# Write a Python program to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number
# class py_solution:
#    def twoSum(self, nums, target):
#         lookup = {}
#         for i, num in enumerate(nums):
#             if target - num in lookup:
#                 return (lookup[target - num], i )
#             lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))



# Write a Python class to find the three elements that sum to zero from a set of n real numbers
# class sep:
#     def func(self,lis):
#         count=[]
#         for i in range(len(lis)):
#             for j in range(i+1,len(lis)):
#                 for k in range(j+1,len(lis)):
#                     if lis[i]==lis[j]==lis[k]:
#                         continue
#                     else:
#                         if(lis[i]+lis[j]+lis[k]==0):
#                             count.append([lis[i],lis[j],lis[k]])
#         return count
# print(sep().func([-25, -10, -7, -3, 2, 4, 8, 10]))



# Write a Python class to reverse a string word by word.
# class clas:
#     def func(self,stra):
#         c=""
#         b=str(stra).split(" ")
#
#         for i in range(len(b)):
#             print(c.join(b[len(b)-i-1]),end=" ")
#         return c
# print(clas().func("hello .py"))



# Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case
# class clas():
#     def __init__(self):
#         self.stra = ""
#
#     def get_String(self):
#         self.stra=input()
#
#     def print_String(self):
#         print(self.stra.upper())
# str1=clas()
# str1.get_String()
# str1.print_String()



# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
# class rect:
#     def __init__(self,l,b):
#         self.length=l
#         self.breath=b
#     def area(self):
#         return self.length*self.breath
# a=rect(3,5)
# print(a.area())



# Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle
# class circle:
#     def __init__(self,r):
#         self.radius=r
#     def peri(self):
#         return "Perimeter is:",self.radius*2*3.14
#     def area(self):
#         return "Area is:",(self.radius**2)*3.14
# c=circle(3)
# print(c.peri())
# print(c.area())



# Write a Python program to get the class name of an instance in Python
# import itertools
# x = itertools.cycle('ABCD')
# print(type(x).__name__)
