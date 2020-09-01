# Write a Python program to create an Enum object and display a member name and value
# from enum import Enum
# class clas(Enum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# print(f"Member name:{clas.Antarctica.name}")
# print(f"Member number:{clas.Antarctica.value}")



# Write a Python program to iterate over an enum class and display individual member and their value
# from enum import Enum
# class clas(Enum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# for data in clas:
#     print(f"{data.name}:{data.value}")



# Write a Python program to display all the member name of an enum class ordered by their values.
# import enum
# class Country(enum.IntEnum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# print('Country Name ordered by Country Code:')
# print('\n'.join('  ' + c.name for c in sorted(Country)))



# Write a Python program to get all values from an enum class
# import enum
# class Country(enum.IntEnum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# print('\n'.join(" "+str(c.value) for c in sorted(Country)))



# Write a Python program to count the most common words in a dictionary
# lis=['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
#    'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
#    'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
#    'white', 'orange', "orange", 'red']
# from collections import Counter
# word_counts=Counter(lis)
# top4=word_counts.most_common(4)
# print(top4)



# Write a Python program to find the class wise roll number from a tuple-of-tuples
# from collections import defaultdict
# classes = (
#     ('V', 1),
#     ('VII', 1),
#     ('V', 2),
#     ('VI', 2),
#     ('VI', 3),
#     ('VII', 1),
# )
# dic=defaultdict(list)
# for name,val in classes:
#     dic[name].append(val)
# print(dic)



# Write a Python program to count the number of students of individual class
# classes = (
# ('V', 1),
# ('VI', 1),
# ('V', 2),
# ('VI', 2),
# ('VI', 3),
# ('VII', 1),
# )
# from collections import Counter
# dic=dict()
# for c,v in classes:
#     dic[c]=v
# print(dic)



# Write a Python program to group a sequence of key-value pairs into a dictionary of list
# from collections import defaultdict
# class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
# d = defaultdict(list)
# for k, v in class_roll:
#     d[k].append(v)
# print(sorted(d.items()))



# Write a Python program to compare two unordered lists (not sets)
# def func(n1,n2):
#     from collections import Counter
#     return Counter(n1)==Counter(n2)



# Write a Python program to get an array buffer information
# from array import array
# a=array('i',[1,2,34,5])
# print(a.buffer_info())



# Write a Python program to convert an array to an array of machine values and return the bytes representation.
# import array
# import binascii
# a = array.array('i', [1,2,3,4,5,6])
# print("Original array:")
# print('A1:', a)
# bytes_array = a.tobytes()
# print('Array of bytes:', binascii.hexlify(bytes_array))



# Write a Python program to push three items into a heap and return the smallest item from the heap.
# Also Pop and return the smallest item from the heap
# import heapq as hq
# heap=[]
# hq.heappush(heap,3)
# hq.heappush(heap,1)
# hq.heappush(heap,2)
# hq.heapify(heap)
# print("The smallest element:",hq.heappop(heap))
# print(heap)



# Write a Python program to get the two largest and three smallest items from a dataset.
# lis=[1,2,3,4,5,6,7,8,9]
# from heapq import nlargest,nsmallest
# largest=nlargest(2,lis)
# print("The largest 2:",largest)
# smaller=nsmallest(3,lis)
# print("The smallest 3:",smaller)



# Write a Python program to locate the right insertion point for a specified value in sorted order
# import bisect
# def func(a,n):
#     return bisect.bisect_right(a,n)
# print(func([1,2,3,4,5],4))


# Write a Python program to find whether a queue is empty or not
# import queue
# q=queue.Queue()
# if q.empty():
#     print(True)



# Write a Python program to create a FIFO queue.
# import queue
# q=queue.Queue()
# for i in range(4):
#     q.put(str(i))



# Write a Python program to create a LIFO queue.
# import queue
# q=queue.LifoQueue()
# for i in range(4):
#     q.put(str(i))



