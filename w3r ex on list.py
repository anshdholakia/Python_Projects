# Write a Python program to generate a 3*4*6 3D array whose each element is *.
# array=[[['*'for col in range(6)]for col in range(4)]for row in range(3)]
# print(array)



# Write a Python program to generate all permutations of a list in Python.
# import itertools
# print(list(itertools.permutations([1,2,3])))



# Write a Python program to get the difference between the two lists.
# lis1=[1,2,34,5,4]
# lis2=[222,2323,222,12,1,22,34]
# sym_diffa=list(set(lis1)-set(lis2))
# sym_diffb=list(set(lis2)-set(lis1))
# total_diff=sym_diffa+sym_diffb
# print(total_diff)



# Write a Python program to flatten a shallow list
# import itertools
# lis=[[2,3,4],[5,6,7],[1,2,3],[7,8,9]]
# merged_list=list(itertools.chain(*lis))
# print(merged_list)



# Write a python program to check whether two lists are circularly identical.
# lis1=[1,2,3,4,5,6,7,8,9]
# lis2=[1,2,3,4,5,6,7,8]
# print(set(lis1).difference(set(lis2))==set())



# Write a Python program to get unique values from a list.
# lis=[20,20,20,40,30,40,2030,3,10,10]
# mylis=set(lis)
# lis2=list(mylis)
# print(lis2)



# frequency of element in list
# lis=[20,30,20,40,50,30,1,4,4,2]
# import collections
# lis2=collections.Counter(lis)
# print(lis2)



# Write a Python program to check whether a list contains a sublist
# def func(lis,lis1):
#     lis3=set()
#     for i in range(len(lis1)):
#         lis3.add(lis1[i])
#     if set(lis).intersection(set(lis1))==lis3:
#         return True
#     else:return False
#
# print(func([2,3,4,5,6,1],[0,1]))



# Write a Python program to generate all sublists of a list
# from itertools import combinations
# def func(lis):
#     result=[]
#     for i in range(0,len(lis)+1):
#         lis2=[list(x) for x in combinations(lis,i)]
#         if len(lis2)>0:
#             result.extend(lis2)
#     return result
# print(func([2,3,4,5]))



# Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)
#
# print(prime_eratosthenes(1000))



# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# def func(lis,n):
#     result=['{}{}'.format(x,y) for y in range(1,n+1) for x in lis]
#     return result
# print(func(["p","q"],5))



# Write a Python program to find common items from two lists.
# lis1=[2,3,4,2,4,2,1,4,2,4,3,4,5,5,3,5,7,4,23,34,34,234,1234]
# lis2=[3,34,23,23,2345,3,23,2,2,3232,3,3,4,2,3,4,2,32,23,3,234,12,4]
# print(set(lis1).intersection(set(lis2)))



# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# lis=[0,1,2,3,4,5]
# for i in range(0,(len(lis)-1),2):
#     lis[i],lis[i+1]=lis[i+1],lis[i]
# print(lis)



# Write a Python program to insert an element before each element of a list.
# color=['red','blue','green']
# color=[v for elt in color for v in ("c",elt)]
# print(color)



# Write a Python program to convert list to list of dictionaries. Go to the editor
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# lis= ["Black", "Red", "Maroon", "Yellow"]
# colour_code=["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'colour name':f,'colour code':z} for f,z in zip(lis,colour_code)])



# Write a Python program to insert a given string at the beginning of all items in a list.
# lis=[1,2,3,4]
# print(['emp{0}'.format(i) for i in lis])



# Write a Python program to find the list in a list of lists whose sum of elements is the highest
# def func(lis):
#     result = 0
#     for j in range(len(lis)): # i=0,1,2,3
#         result+=int(lis[j])
#     return result
# def func2(lis2):
#     max_value=0
#     res=[]
#     for i in range(len(lis2)):
#         if(func(lis2[i])>max_value):
#             res=lis2[i]
#             max_value=func(lis2[i])
#     return res
# print(func2([[2,3,4],[4,5,6],[8,10,20],[3,6,7]]))



# Write a Python program to remove duplicates from a list of lists.
# lis=[[2,3,4],[2,3,4],[10],[1,2,3],[4],[10],[7,8,9],[6],[7]]
# res=[]
# for i in range(len(lis)):
#     if lis[i] not in res:
#         res.append(lis[i])
#     else:continue
# print(res)




# Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# def func(lis,num):
#     return [lis[:num]]+[lis[num:]]
# print(func([1, 1, 2, 3, 4, 4, 5, 1],4))



# write a python program to round every number of a
# given list of numbers and print the total sum multiplied by the length of the list.
# lis=[22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
# length=len(lis)
# result=sum(list(map(round,lis))*length)
# print(result)



