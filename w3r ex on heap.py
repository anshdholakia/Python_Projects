# using heap algorithm obtain three largest numebrs from a list
# lis=[2,3,2,4,353,4,4545,465443,34,33,4545,3224,2334346,54756]
# from heapq import nlargest
# print(nlargest(3,lis))



# Write a Python program to find the three smallest integers from
# a given list of numbers using Heap queue algorithm
# import heapq as hq
# lis=[2,3,2,4,353,4,4545,465443,34,33,4545,3224,2334346,54756]
# print(hq.nsmallest(3,lis))



# Write a Python program to implement a heapsort by
# pushing all values onto a heap and then popping off the smallest values one at a time
# import heapq as hq
# def func(lis):
#     h=[]
#     for i in lis:
#         hq.heappush(h,i)
#     return [hq.heappop(h) for i in range(len(h))]
# print(func([2,3,2,4,353,4,4545,465443,34,33,4545,3224,2334346,54756]))




# Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm.
# lis=[2,3,4,5,5,3,21,1,3455,35,56,7,543,2,23,23,1,4,2387]
# import heapq as hq
# hq.heapify(lis)
# print(lis)



# Write a Python program to delete the smallest element from the given Heap and then inserts a new item.
# lis=[2,3,4,5,4,5,6,4,5,54,5,4]
# import heapq as hq
# hq.heapify(lis)
# hq.heapreplace(lis,356)  # replaces the smallest element with 356
# print(lis)



# Write a Python program to find the kth (1 <= k <= array's length) largest element
# in an unsorted array using Heap queue algorithm.
# lis=[2,3,4,34,3,5575,686757,434,2,1,3,3,5,3,56]
# import heapq as hq
# hq.heapify(lis)
# print(hq.nlargest(1,lis))



# Write a Python program to find the top k integers that occur the most
# frequently from a given lists of sorted and distinct integers using Heap queue algorithm
# lis=[2,3,4,34,3,5575,686757,434,2,1,3,3,5,3,56]
# import heapq
# heapq.heapify(lis)
# print(lis)



# Write a Python program to get the n expensive and cheap price items from a given dataset using Heap queue algorithm.
# def func(lis,k):
#     import heapq as hq
#     import collections
#     prices=[]
#     costly=[]
#     cheap=[]
#     if (len(lis)/2)<k:
#         return f"incorrect input"
#
#     for i in range(len(lis)):
#         prices.append(lis[i].get('price'))
#     hq.heapify(prices)
#     print(f"The costly top {k} prices:\n")
#     for i in range(len(lis)):
#         for z in range(k):
#             if(lis[i].get('price')==prices[len(prices)-z-1]):
#                 print(lis[i])
#
#
#
# a=[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75},{'name': 'Item-5', 'price': 16.3},{'name': 'Item-6', 'price': 110.65}]
# print(func(a,3))




# write a python program to check if the letters of a given string can be rearranged
# so that two characters that are adjacent to each other are different using Heap queue algorithm.
# import heapq as hq
# a=input('Enter a string:\n')
# lis=[]
# lis2=[]
# temp=[]
# for i in range(len(a)):
#     lis.append(a[i])
#
# for i in range(0,len(lis)):
#     for j in range(1,len(lis2)):
#         if lis2[j]==lis2[j-1]:
#             temp.append(hq.heappop(lis2))
#     lis2.append(lis[i])
# for i in temp:
#     hq.heappush(lis2,i)
# print(list(lis2))




# You are given two integer arrays sorted in ascending order and an integer k
# Write a Python program to find k number of pairs (u, v) which consists of one element from the
# first array and one element from the second array using Heap queue algorithm.
# import heapq as hq
# def func(lis1,lis2):
#     k=0
#     results=[]
#     for i in lis1:
#         for j in lis2:
#             if (i!=j):
#                 hq.heappush(results,(i,j))
#                 k+=1
#     return f"{k}"
#
# print(func([1,2],[1,4]))




# Write a Python program to print a heap as a tree-like data structure.
import math
from io import StringIO
#source https://bit.ly/38HXSoU
# def show_tree(tree, total_width=60, fill=' '):
#     """Pretty-print a tree.
#     total_width depends on your input size"""
#     output = StringIO()
#     last_row = -1
#     for i, n in enumerate(tree):
#         if i:
#             row = int(math.floor(math.log(i+1, 2)))
#         else:
#             row = 0
#         if row != last_row:
#             output.write('\n')
#         columns = 2**row
#         col_width = int(math.floor((total_width * 1.0) / columns))
#         output.write(str(n).center(col_width, fill))
#         last_row = row
#     print (output.getvalue())
#     print ('-' * total_width)
#     return
#
# #test
# import heapq
# heap = []
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 7)
# heapq.heappush(heap, 9)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 8)
# heapq.heappush(heap, 16)
# heapq.heappush(heap, 14)
# show_tree(heap)
