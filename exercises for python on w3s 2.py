#
# import os,platform
# print(os.name)
# print("\n")
# print(platform.system())
# print("\n")
# print(platform.version())
#
#
# creating all possible strings using vowels
# lis=['a','e','i','o','u']
# import random
#
# for i in range(0,120):
#     random.shuffle(lis)
#     print(''.join(lis))
#
#
#
# to make a list out of list that when added triplets gives 0
# def three_sum(nums):
#   result = []
#   nums.sort()
#   for i in range(len(nums)-2):
#     if i> 0 and nums[i] == nums[i-1]:
#       continue
#     l, r = i+1, len(nums)-1
#     while l < r:
#       s = nums[i] + nums[l] + nums[r]
#       if s > 0:
#         r -= 1
#       elif s < 0:
#           l += 1
#       else:
#         # found three sum
#         result.append((nums[i], nums[l], nums[r]))
#         # remove duplicates
#         while l < r and nums[l] == nums[l+1]:
#           l+=1
#           while l < r and nums[r] == nums[r-1]:
#             r -= 1
#             l += 1
#             r -= 1
#           return result
#
# x = [1, -6, 4, 2, -1, 0, 0, -2, 0 ]
# print(three_sum(x))
#
# how to count every letter in a text file
# import collections
# import pprint
#
# with open("ansh.txt") as data:
#     count=collections.Counter(data.read().lower())
#     value=pprint.pformat(count)
# print(value)
#
# printing os
# import pkg_resources
# packages=pkg_resources.working_set
# package_list=sorted(["%s==%s"% (i.key,i.version)
#                      for i in packages])
# for m in package_list:
#   print(m)
#
# checking if numbers in different x,y z are summed up and are closer ot target value
#
# import itertools
# from functools import partial
# X=[1,2,3]
# Y=[3,4,2]
# Z=[12,33,1]
# T=7
#
# def check(num,*nums):
#     if sum(x for x in nums)==num:
#         return (True,nums)
#     else:
#         return (False,nums)
# pro=itertools.product(X,Y,Z)
# func=partial(check,T)
# sums=list(itertools.starmap(func,pro))
#
# result=set()
# for m in sums:
#     if m[0]==True and m[1] not in result:
#         result.add(m[1])
#         print(result)
#
# random list of list of numbers
# def permute(nums):
#   result_perms = [[]]
#   for n in nums:
#     new_perms = []
#     for perm in result_perms:
#       for i in range(len(perm)+1):
#         new_perms.append(perm[:i] + [n] + perm[i:])
#         result_perms = new_perms
#   return result_perms
#
# my_nums = [2,2,12,2331,23]
# print("Original Collection: ",my_nums)
# print("Collection of distinct numbers:\n",permute(my_nums))
#
# Python program to get all possible two digit letter combinations
# string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#
# def appen(digit):
#     if digit=="":
#         return []
#
#     result=[""]
#     for num in digit:
#         temp=[]
#         for a in result:
#             for cha in string_maps[num]:
#                 temp.append(a+cha)
#         result=temp
#     return result
#
#
# print(appen("24"))
#
# add two numbers without '+' sign using bitwise operators
# def add(a,b):
#     while b!=0:
#         num=a & b
#         a= a^b
#         b=num<<1
#     return a
#
# print(add(10,1))
#
# checking the power of operators
# from collections import deque
# import re
#
# __operators__="+-/*"
# __parenthesis__="()"
# __priority__={
#     '+':0,
#     '-':0,
#     '*':1,
#     '/':1,
# }
# def test_higher_priority(operator1,operator2):
#     return __priority__[operator1]>=__priority__[operator2]
#
# print(test_higher_priority("+","*"))
#
# printing strobo-grammatic numbers
# def gen(n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     result=resul(n,n)
#     return result
#
#
# def resul(n,length):
#     if n==0:
#         return [""]
#     if n==1:
#         return ["0","8","1"]
#
#     middles=resul(n-2,length)
#     result=[]
#     for middle in middles:
#         if n!=length:
#             result.append("0"+middle+"0")
#         result.append("8"+middle+"8")
#         result.append("6"+middle+"9")
#         result.append("9"+middle+"6")
#         result.append("1"+middle+"1")
#     return result
# print("When n=5:\n",gen(5))
#
# determining power of 2
# def ndegrees(num):
#   ans = True
#   n, tempn, i = 2, 2, 2
#   while ans:
#     if str(tempn) in num:
#       i += 1
#       tempn = pow(n, i)
#     else:
#       ans = False
#
#     if i-1==1:
#         return 0
#
#
#   return i-1
# print(ndegrees("2"))
# print(ndegrees("2481632"))
#
# count the number of zeros in a factorial
# def factendzero(n):
#     x = n // 5
#     y = x
#     while x > 0:
#         x /= 5
#         y += int(x)
#     return y
#
#
# p=int(input("Enter a number:"))
# print("The number of zeroes in its factorial is :",factendzero(p))
#
# Write a Python program to create a sequence where the first four members of the
# sequence are equal to one, and each successive term of the sequence is equal
# to the sum of the four previous ones. Find the Nth member of the sequence.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# to find out the number of odd and even divisors
# def div(n):
#     lise=[]
#     liso=[]
#     for i in range(1,n):
#         if n%i==0 and i%2==0:
#             lise.append(i)
#         if n % i == 0 and i % 2 == 1:
#             liso.append(i)
#     return f'Odd divisors {len(liso)+len(lise)} and even divisors'
#
# print(div(40))
#
#
# to find missing numbers in a phone number
# def sep(number):
#     no_of_numbers=set([1,2,3,4,5,6,7,8,9,0])
#     number=set([int(i) for i in number])
#     number=number.symmetric_difference(no_of_numbers)
#     number=sorted(number)
#     return number
#
# print(sep([7,8,7,4,8,7,1,4,9,1]))
#
#
# finding AP and GP
# def ap(set):
#     lis=[]
#     a=set[0]
#     if set[1]-set[0]==set[2]-set[1]:
#         d=set[1]-set[0]
#         for i in range(0,100):
#             lis.append(a+i*d)
#         return lis
#
#     else:return f"Please enter valid sequence"
#
# def gp(et):
#     lip=[]
#     a=et[0]
#     if et[1]/et[0]==et[2]/et[1]:
#         r=et[1]/et[0]
#         for i in range(0,100):
#             lip.append(a*(r**i))
#
#     return lip
#
# print(f"This is the AP list {ap([1,3,5])}\n and this is the GP list {gp([3,9,27])}")
#
#
# take an input number that reverses and adds it to itslef that gives a palindrom number
# def palindorm(num):
#     reverse=0
#     i=num
#     while(i!=0):
#         reverse=((reverse*10)+(i%10))
#         i=int(i/10)
#     sum=reverse+num
#     sumrev=0
#     n = sum
#     while (n != 0):
#         sumrev = ((sumrev * 10) + (n % 10))
#         n = int(n / 10)
#     if sumrev==sum:
#         return f"Yes the sum of {num} and its palindrom {reverse} is a palindrom number:{sumrev}"
#     else:
#         return f"Its sum is not a palindrom"
#
#
#
# a=int(input("Enter a number you want to check if it is a palindrom or not\n"))
# print(palindorm(a))
#
#
# triangle guesser, right or valid or incorrect
# import math
# def nums(num):
#     a=str(num).split(" ") #a is a list
#     if int(a[0])>int(a[1])+int(a[2]) or int(a[1])>int(a[0])+int(a[2]) or int(a[2])>int(a[1])+int(a[0]):
#         print("Restart and give valid inputs!, Not a valid traingle\n")
#
#     elif int(a[0])==math.sqrt(int(a[1])**2+int(a[2])**2) or int(a[2])==math.sqrt(int(a[1])**2+int(a[0])**2) or int(a[1])==math.sqrt(int(a[0])**2+int(a[2])**2):
#         print("It is a Right angle triangle\n")
#
#     else:
#         print("It is a valid triangle, but not a right angled triangle\n")
#
# a=input("Provide me with sides separated by blank:\n")
# nums(a)
#
#
# amount of loan after some months
# def loan(month):
#     debt=float(5/100)
#     rs=float(100000)
#     total=(rs)*(debt**month)
#     return total
#
# a=int(input("Enter the number of months you want\n"))
# print("Number of months:",a,"\n")
#
# print(loan(a))
#
#
# to print prime numbers below a certain number
# import math
# def pri(num):
#     lis=[]
#     if num>1:
#
#         for i in range(2,num):
#                 if num%i==0:
#                     continue
#                 else:
#                     lis.append(i)
#         return lis
#
#
# print(pri(15))
#
#
#
#
# There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2).
# Write a Python program to test the followings -
#
# "C2 is in C1" if C2 is in C1
# "C1 is in C2" if C1 is in C2
# "Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect, and
# "C1 and C2 do not overlap" if C1 and C2 do not overlap.
#
# Input:
# Input numbers (real numbers) are separated by a space.
# Input x1, y1, r1, x2, y2, r2:
# 5 6 4 8 7 9
# C1 is in C2
# import math
# def function(num):
#     x1,y1,r1,x2,y2,r2=str(num).split(" ")
#     d=math.sqrt((int(x1)-int(x2))**2+(int(y1)-int(y2))**2)
#     if d < int(r1) - int(r2):
#         return "C2  is in C1"
#     elif d < int(r2) - int(r1):
#         return "C1  is in C2"
#     elif d > int(r1) + int(r2):
#         return "Circumference of C1  and C2  intersect"
#     else:
#         return "C1 and C2  do not overlap"
#
# print(function("22 2 3 4 5 7"))
#
#
#
#
# Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year. Go to the editor
# Input:
# Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
# Input month and date (separated by a single space):
# 5 15
# Name of the date: Sunday
# from datetime import date
# def function(num):
#     m,d=str(num).split(" ")
#     weeks={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
#     w=date.isoweekday(date(2016,int(m),int(d)))
#     return weeks[w]
#
# print(function("6 14"))
#
#
#
# Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.
# a=input("Enter a string:\n")
# lis=a.split()
# for i in range(len(lis)):
#     if "Python" in lis[i]:n=lis[i].index("Python");lis[i]=lis[i][:n] +"Java" +lis[i][n+6:]
#     elif "Java" in lis[i]: n = lis[i].index("Java");lis[i] = lis[i][:n] + "Python" + lis[i][n + 4:]
# print(*lis)
#
#
# write a program that reverses a number to the highest and lowest and gives its difference
#
# def func(n):
#     lis=list(str(n))
#     print("The difference between the largest and the smallest integer is:\n")
#     b=(int("".join(sorted(lis,reverse=True)))-int("".join(sorted(lis))))
#     return b
# a=int(input("Enter a 8 digit number containing numbers between 0-9:\n"))
# print(func(a))
#
#
#
# sum of n prime numbers
# def func(num):
#     lis=[]
#     c=3
#     while(num>len(list(lis))):
#         for i in range(2,c):
#
#     return lis
#
# print(func(5))
#
#
# if you draw a straight line on a plane, the plane is divided into two regions. For example,
# if you pull two straight lines in parallel, you get three areas, and if you draw
# vertically one to the other you get 4 areas.
# Write a Python program to create maximum number of regions obtained by drawing n given straight lines.
# def func(nl):
#     return (nl*2)+(nl+1)
# print(func(3))
#
#
# There are 10 vertical and horizontal squares on a plane.
# Each square is painted blue and green. Blue represents the sea, and green represents the land.
# When two green squares are in contact with the top and bottom, or right and left,
# they are said to be ground. The area created by only one green square is called "island".
# For example, there are five islands in the figure below.
# Write a Python program to read the mass data and find the number of islands.
# def func(stra):
#     b=""
#     str=[]
#     i=0
#     for l in stra:
#         str.append(l)
#     for k in range(0,len(str)):
#         if(str[k]=="#"):
#             str.insert(k+2,(int(str[k+1])-1)*str[k+2])
#             str.pop(k+1)
#             i+=1
#         else:continue
#     for e in range(0,i):
#         str.remove("#")
#     return b.join(str)
# print(func("XY#6Z1#5023"))
#
#
#
# There are 10 vertical and horizontal squares on a plane.
# Each square is painted blue and green. Blue represents the sea, and green represents the land.
# When two green squares are in contact with the top and bottom, or right and left, they are said to be ground.
# The area created by only one green square is called "island". For example, there are five islands in the figure below.
# c=0
# def f(x,y,z):
#     if 0<=y<10 and 0<=z<10 and x[z][y]=='1':
#         x[z][y]='0'
#         for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:f(x,y+dy,z+dz)
# print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros")
# while 1:
#     try:
#         if c:input()
#     except:break
#     x = [list(input()) for _ in [0]*10]
#     c=1;b=0
#     for i in range(10):
#         for j in range(10):
#             if x[j][i]=='1':
#                 b+=1;f(x,i,j)
#     print("Number of islands:")
#     print(b)
#
#
# Write a Python program to cut out words of 3 to 6 characters length
# from a given sentence not more than 1024 characters.
# def func(stra):
#     a=[]
#     b=""
#     lis=str(stra).split(" ")
#     for i in range(0,len(lis)):
#         if 2<int(len(lis[i]))<6:
#             a.append(lis[i]+" ")
#         else:continue
#     return b.join(a)
# print(func("My name is Ansh Dholakia"))
#
#
# Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge,
# when starting from the top and proceeding according to the next rule to the bottom.
# Write a Python program that compute the maximum value of the sum of the passing integers according to the following rules.
# At each step, you can go to the lower left diagonal or the lower right diagonal.
# For example, in the example of FIG. 1, as shown in FIG. 2, when 8,4,9,8,6,8,9,4,8 is selected and passed,
# the sum is 64 (8 + 4 + 9) + 8 + 6 + 8 + 9 + 4 + 8 = 64)
# import sys
# print("Input the numbers (ctrl+d to exit):")
# x = [list(map(int, l.split(","))) for l in sys.stdin]
# dp = x[0]
#
# for i in range(1, (len(x) + 1) // 2):
#     _dp = [0] * (i + 1)
#     for j in range(i):
#         _dp[j] = max(_dp[j], dp[j] + x[i][j])
#         _dp[j + 1] = max(_dp[j + 1], dp[j] + x[i][j + 1])
#     dp = _dp
#
# for i in range((len(x) + 1) // 2, len(x)):
#     _dp = [0] * (len(dp) - 1)
#     for j in range(len(_dp)):
#         _dp[j] = max(dp[j], dp[j + 1]) + x[i][j]
#     dp = _dp
# print("Maximum value of the sum of integers passing according to the rule on one line.")
# print(dp[0])
#
#
# Given a list of numbers and a number k,
# write a Python program to check whether the sum of any two numbers from the list is equal to k or not.
# For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
# import random
# def func(lis):
#     k=16
#     for i in range(0,len(list(lis))*(len(list(lis))-1)):
#         s=random.sample(list(lis),2)
#         if (int(s[0])+int(s[1])==k):
#             return f"{s[0]} + {s[1]} is {k}"
#         else:continue
#
# print(func([1,2,3,4,5,6,7,8,9,10]))
#
#
# The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above
# string (A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
# The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape",
# "ale", "appl", "appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
# Write a Python program to find the longest word in set of words which is a subsequence of a given string.
# def func(stra):
#     import random
#     lis=[]
#     a=[]
#     for i in range(0,len(str(stra))):
#         lis.append(stra[i])
#     for i in range(len(lis)-1):
#         for j in range(len(lis)):
#             a.append(lis[i]+lis[j])
#             j = i + 1
#     return a
# print(func("ansh"))
#
#
# #A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers
# for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# Write a Python program to check whether a number is "happy" or not.
# def func(num):
#     lis=[]
#     sum2=0
#     b=str(num)
#     while (num!= 1):
#         sum1=0
#         num=str(num)
#         for l in range(0,len(num)):
#             sum1+=(int(num[l])**2)
#         num = sum1
#     if(num==1):
#         return "True"
#     else:
#         return "False"
#
#
# print(func("7"))
#
#
# Write a Python program to count the number of prime numbers less than a given non-negative number.
# def count_Primes_nums(n):
#     ctr = 0
#     for num in range(n):
#         if num <= 1:
#             continue
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             ctr += 1
#     return ctr
#
# print(count_Primes_nums(10))
# print(count_Primes_nums(100))
#
#
# Write a Python program to find the longest common prefix string amongst a given array of strings.
# Return false If there is no common prefix.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
# def func(str1,str2):
#     b=""
#     lis=[]
#     for i in range(0,len(str(str1))):
#         for k in range(0,len(str(str2))):
#             if (str1[i]==str2[k]):
#                 lis.append(str1[i])
#                 break
#             else:
#                 continue
#
#     return b.join(lis)
#
# print(func("abcdefgh","abcefgh"))
#
#
#
# Write a Python program to check whether a given integer is a palindrome or not.
# def func(num):
#     return str(num)==str(num)[::-1]
#
# print(func("222"))
#
#
#
# Write a Python program to remove the duplicate elements of a given array
# of numbers such that each element appear only once and return the new length of the given array.
# def func(lis):
#     lis2=[]
#     for i in range(0,len(list(lis))):
#         if lis[i] not in lis2:lis2.append(lis[i])
#         else:continue
#     return f"The list is {lis2} and the length of list is {len(lis2)}"
# print(func([1, 2, 2, 3, 4, 4,1]))
#
#
# Write a Python program to calculate the maximum profit from selling and buying values of stock.
# An array of numbers represent the stock prices in chronological order.
# def buy_and_sell(stock_price):
#     max_profit_val, current_max_val = 0, 0
#     for price in reversed(stock_price):
#         current_max_val = max(current_max_val, price)
#         potential_profit = current_max_val - price
#         max_profit_val = max(potential_profit, max_profit_val)
#
#     return max_profit_val
#
# print(buy_and_sell([8, 10, 7, 5, 7, 15]))
# print(buy_and_sell([1, 2, 8, 1]))
# print(buy_and_sell([]))
#
#
# #The price of a given stock on each day is stored in an array.
# Write a Python program to find the maximum profit in one transaction i.e., buy one and sell one share of the stock
# from the given price value of the said array. You cannot sell a stock before you buy one.
# def func(lis):
#     result=[]
#     for i in range(len(list(lis))):
#
#         for j in range(len(list(lis))):
#
#             if (lis[i]==lis[j]):
#                 continue
#             else:
#                 b=lis[i]-lis[j]
#                 result.append(b)
#     result.sort()
#     result.reverse()
#     return result[0]
#
# print(func([224, 236, 247, 258, 259, 225]))
#
#
# Write a Python program to print a given N by M matrix of numbers line by line in forward > backwards > forward >... order.
# def func(lis):
#     for i in range(0,len(list(lis))):
#         if(i==0 or i==2):
#             for j in range(0,len(list(lis))):
#                 print(f"{lis[i][j]}")
#         else:
#             for j in range(0,len(list(lis))):
#                 print(f"{lis[i][len(list(lis))-j-1]}")
#
# func([[1, 2, 3,4],[5, 6, 7, 8],[0, 6, 2, 8],[2, 3, 0, 2]])
#
#
#
# Write a Python program to randomly generate a list with 10 even numbers between 1 and 100 inclusive.
# import random
# lis=[]
# for i in range(0,100):
#     if(i%2==0):
#         lis.append(i)
# print(random.sample(lis,10))
#
# python code to find median
# def func(lis):
#     lis.sort()
#     m=len(lis)//2
#     if len(lis)%2==0:
#         return (lis[m-1]+lis[m])/2
#     else:
#         return lis[m]
#
# print(func([1.0,2.11,3.3,4.2,5.22,6.55]))
#
#
# palindorm
# def func(num):
#     i=len(num)
#     rev=0
#     a=int(num)
#     b=int(num)
#     while(i!=0):
#         rev=(rev*10+(a%10))
#         a=int(a/10)
#         i-=1
#     if rev==int(num):
#         return True
#     else: return False
# print(func("333"))
#
#
# Write a Python program that accept a list of numbers and create a list to store the
# count of negative number in first element and store the sum of positive numbers in second element.
# def func(num):
#     p=0
#     n=0
#     lis=[]
#     for i in range(len(list(num))):
#         if num[i]>=0:
#             p+=1
#         else:
#             n+=1
#     lis.append(n)
#     lis.append(p)
#     return lis
# print(func([-1, -2, -3, -4, -5]))
#
#
# Write a Python program to check whether a given string is an "isogram" or not.
# def func(stra):
#     return len(stra)==len(set(stra.lower()))
# print(func("python"))
#
#
#
# Write a Python program to count the number of equal numbers from three given integers.
# def func(z,b,c):
#     a=0
#     for i in range(len(str(z))):
#         for j in range(len(str(b))):
#             for k in range(len(str(c))):
#                 if z[i]==b[j]==c[k]:
#                     a+=3
#                     break
#                 elif z[i]==b[j]:
#                     a+=2
#                     break
#                 elif c[k]==b[j]:
#                     a+=2
#                     break
#                 elif z[i]==c[k]:
#                     a+=2
#                     break
#     return a
# print(func("1","3","2"))
#
#
# Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits.
# Return True if the employee code is valid and False if it's not.
# def func(num):
#     if len(num)==8 or len(num)==12:return True
#     else:return False
# print(func("2364768"))
#
#
# Write a Python program that accept two strings and test if the letters in the second string are present in the first string.
# def func(stra,strb):
#     lisa=[]
#     lisb=[]
#     for i in range(len(str(stra))):
#         lisa.append(stra[i])
#     for j in range(len(str(strb))):
#         lisb.append(strb[j])
#     if set(lisa).intersection(set(lisb))==set(lisb):
#         return True
#     else:
#         return False
# print(func("python", "ypthon"))
#
#
#
# Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers.
# def func(lis):
#     lis.sort()
#     return lis[0]+lis[1]+lis[2]
#
# print(func([1,2,3,4,5,7,7,8,6,433,23,32,0]))
#
#
#
# Write a Python program to find the middle character(s) of a given string.
# If the length of the string is odd return the middle character and return the middle two characters if the string length is even.
# def func(stra):
#     if len(stra)%2==0:
#         return f"{stra[int((len(stra)/2)-1)]}{stra[int(len(stra)/2)]}"
#     else:
#         return f"{stra[int(len(stra)/2)]}"
# print(func(""))
#
#
#
# Write a Python program to compute
# the sum of all items of a given array of integers where each integer is multiplied by its index. Return 0 if there is no number.
# def func(lis):
#     a=0
#     if len(lis)==0:
#         return 0
#     else:
#         for i in range(len(lis)):
#             a+=lis[i]*i
#         return a
# print(func([1,2,3,4]))
#
#
# Write a Python program to find the position
# of the second occurrence of a given string in another given string. If there is no such string return -1.
# def find_string(txt, str1):
#     return txt.find(str1, txt.find(str1) + 1)
#
# print(find_string("wefwe abcde","abcde"))
#
#
#
# Write a Python program to create a new string with no duplicate consecutive letters from a given string.
# def func(stra):
#     b=""
#     lis=[]
#     for i in range(len(stra)):
#         if stra[i]==stra[i-1]:
#             lis.append(stra[i])
#             lis.pop(i-1)
#         else:lis.append(stra[i])
#     return b.join(lis)
# print(func("ppttedsd"))




# Write a Python program to test whether a given integer is pandigital number or not.
# def func(num):
#     lis=[]
#     for i in range(len(num)):
#         lis.append(num[i])
#     b=set(lis)
#     return b.intersection([0,1,2,3,4,5,6,7,8,9])
#
# print(func("1234567890"))



# Write a Python program to compute the digit distance between two integers.
# def func(num1,num2):
#     a=0
#     for i in range(len(str(num1))):
#         if(int(num1[i])>int(num2[i])):
#             a+=int(num1[i])-int(num2[i])
#         elif(int(num2[i])>int(num1[i])):
#             a+=int(num2[i])-int(num1[i])
#         else:
#             a+=0
#     return a
# print(func("123","256"))



# Write a Python program to print letters from the English alphabet from a-z and A-Z.
# import string
# print("Letter from a to z")
# for letter in string.ascii_lowercase:
#     print(letter,end=" ")
# print("\n")
# print("\nLetter from A to Z")
# for letter in string.ascii_uppercase:
#     print(letter, end=" ")



# Write a Python program to generate and prints a list of numbers from 1 to 10.
# import string
# print("Numbers from 1 to 10")
# a=''
# lis=[]
# for num in string.digits:
#     lis.append(num)
# lis.remove("0")
# print(lis)



# Write a Python program to identify nonprime numbers between 1 to 100 (integers). Print the nonprime numbers.
# lis=[]
# for i in range(4,101):
#     if i%2==0 or i%3==0:
#         print(i)




# Write a Python program to make a request to a web page, and test the status code,
# also display the html code of the specified web page.
# import requests
# r=requests.get("https://www.w3resource.com/python-exercises/basic/")
# print("Resposive[",r.status_code,"]")
# print(r.text)



# In multiprocessing, processes are spawned by creating a Process object.
# Write a Python program to show the individual process IDs (parent process, process id etc.) involved.
# from multiprocessing import Process
# import os
# def info(title):
#     print(title)
#     print("module name",__name__)
#     print("parent process",os.getppid())
#     print("process id",os.getpid())
# def f(name):
#     info("function f")
#     print("hello",name)
# if __name__ == '__main__':
#     info('Main line')
#     p = Process(target=f, args=('ansh',))
#     p.start()
#     p.join()



# Write a Python program to check if two given numbers are coprime or not.
# Return True if two numbers are coprime otherwise return false.
# def func(num1,num2):
#     lis1=[]
#     lis2=[]
#     for i in range(1,int(num1)):
#         if int(num1)%i==0:
#             lis1.append(i)
#
#     for j in range(1,int(num2)):
#         if int(num2)%j==0:
#             lis2.append(j)
#     if set(lis1).intersection(set(lis2))=={1}:
#         return True
#     else: return False
# print(func("17","13"))




# euclid totiet function
# def gcd(p,q):
# # Create the gcd of two positive integers.
#     while q != 0:
#         p, q = q, p%q
#     return p
#
# def is_coprime(x, y):
#     return gcd(x, y) == 1
#
# def phi_func(x):
#     if x == 1:
#         return 1
#     else:
#         n = [y for y in range(1,x) if is_coprime(x,y)]
#         return len(n)
# print(phi_func(10))
# print(phi_func(15))
# print(phi_func(33))
