# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also
# create a lambda function that multiplies argument x with argument y and print the result.
# a=int(input("Enter a number:\n"))
# add=lambda x:x+15
# print(add(a))
# multilply=lambda x,y:x*y
# a=int(input("Enter a number:\n"))
# b=int(input("Enter a second number:\n"))
# print(multilply(a,b))



#  Write a Python program to create a function that takes one argument,
#  and that argument will be multiplied with an unknown given number.
# multi=lambda x:x*3
# print(multi(int(input("Enter a number:\n"))))



# Write a Python program to sort a list of tuples using Lambda.
# lis=[(1,2,3,4),(5,6,7,8),(1,3,4,2,5)]
# lis.sort(key=lambda x:x[0])
# print(lis)



# Write a Python program to sort a list of dictionaries using Lambda
# dic=[{'subject':'math','marks':32},{'subject':'science','marks':43},{'subject':'english','marks':34},{'subject':'s.s','marks':23}]
# dic.sort(key=lambda x:x['marks'] )
# print(dic)



# Write a Python program to filter a list of integers using Lambda
# lis=[23,5,322,33,242]
# even_nums=list(filter(lambda x:x%2==0,lis))
# odd_nums=list(filter(lambda x:x%2==1,lis))
# print("Even numbers:",even_nums)
# print("Odd numbers:",odd_nums)



# Write a Python program to square and cube every number in a given list of integers using Lambda
# lis=[2,3,4,5,3,2,323,33,3223]
# sq=list(map(lambda x:x*x,lis))
# cube=list(map(lambda x:x*x*x,lis))
# print("Square values of elements:",sq)
# print("Cube values of elements:",cube)



# Write a Python program to find if a given string starts with a given character using Lambda.
# a=input("Enter a string:\n")
# start=lambda stra:True if (stra[0]=='a') else False
# print(start(a))



# Write a Python program to extract year, month, date and time using Lambda.
# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))



# Write a Python program to check whether a given string is number or not using Lambda
# a=input("Enter a number or string:\n")
# check=lambda x:f"It is a number" if x.isnumeric() else "It is a string"
# print(check(a))



# Write a Python program to create Fibonacci series upto n using Lambda.
# a=int(input("Enter the number of terms:\n"))
# from functools import reduce
# fib=lambda b:reduce(lambda x,_:x+[x[-1]+x[-2]],range(b-2),[0,1])
# print(fib(a))



# Write a Python program to find intersection of two given arrays using Lambda
# import array
# func=lambda arr1,arr2:set(arr1).intersection(set(arr2))
# arr1=array.array('i',[1,2,3,4,5])
# arr2=array.array('i',[1,3,5])
# print(func(arr1,arr2))



# Write a Python program to rearrange positive and negative numbers in a given array using Lambda
# a=[1,29093,2,-1,3,33,3232,2313]
# result=[x for x in a if x<0]+[x for x in a if x>0]
# print(result)



# Write a Python program to filter a given list whether the values in the list are having length of 6 using Lambda.
# lis=[214343,324,13234,435345]
# d=filter(lambda b: True if len(str(b))==6 else '',lis)
# for de in d:
#     print(de)



# Write a Python program to add two given lists using map and lambda.
# lis1=[1,2,3,4,5]
# lis2=[6,7,8,9,10,11]
# func=map(lambda x,y:x+y,lis1,lis2)
# print(list(func))



# Write a Python program that multiply each number of given list with a given number
# using lambda function. Print the result
# lis=[1,2,3,4,23,456,23342]
# result=list(map(lambda x:x*3,lis))
# print(result)



# Write a Python program that sum the length of the names of a given list
# of names after removing the names that starts with an lowercase letter. Use lambda function
# lis=['ansh','dholakia','is','a','good','boy']
# result=list(filter(lambda x:x[0]!='a',lis))
# print(len("".join(result)))




# Write a Python program that removes the positive numbers from a given list of numbers.
# Sum the negative numbers and print the absolute value using lambda function. Print the result.
# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# print("Original list: ", nums)
# print("Result:")
# print(abs(sum([i for i in nums if i < 0])))
