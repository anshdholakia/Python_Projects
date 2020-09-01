# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# dic=dict()
# for i in range(1,16):
#     dic[i]=i*i
# print(dic)


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
# dic=dict()
# for i in range(1,6):
#     dic[i]=i*i
# print(dic)



# Write a Python program to get the maximum and minimum value in a dictionary.
# dic={'ansh':2,"lewis":1,"harry":3}
# max=max(dic.values())
# min=min(dic.values())
# print(max)
# print(min)



# Write a Python program to get a dictionary from an object's fields.
# class Dodict(object):
#     def __init__(self):
#         self.x=2
#         self.y=5
#         self.z=7
# test=Dodict()
# print(test.__dict__)



# Write a Python program to remove duplicates from Dictionary
# dic={"ansh":1,"ansh":1,"varun":5}
# res={}
# for key,value in dic.items():
#     if (key not in res):
#         res[key]=value
#     else:continue
# print(res)



# Write a Python program to combine two dictionary adding values for common keys
# d1={"a":100,"b":200,"c":300,"d":300}
# d2={"a":300,"b":200,"e":300,"d":400}
# from collections import Counter
# d=Counter(d1)+Counter(d2)
# print(d)



# Write a Python program to combine values in python list of dictionaries
# lis= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# from collections import Counter
# dic=Counter()
# for d in lis:
#     dic[d['item']]+=d['amount']
# print(dic)



# Write a Python program to create a dictionary from a string
# a=input("Enter a string:\n")
# from collections import Counter
# dic=dict()
# for i in range(len(a)):
#     dic[a[i]]=dic.get(a[i],0)+1
# print(dic)




# Write a Python program to print a dictionary in table format.
# dic={"Ansh":1,"Rohan":2,"Carol":4}
# print("Name       Position\n")
# for k,v in dic.items():
#     print(f"{k}       {dic[k]}\n")



# Write a Python program to count the values associated with key in a dictionary.
# lis=[{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
#      {'id': 3, 'success': True, 'name': 'Alex'}]
# count=0
# for i in range(len(lis)):
#     if(lis[i].get('success')==True):
#         count+=1
# print(count)



# Write a Python program to get the top three items in a shop.
# from heapq import nlargest
# from operator import itemgetter
# di={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for x,y in nlargest(3,di.items(),key=itemgetter(1)):
#     print(x,y)



# Write a Python program to create a dictionary from two lists without losing duplicate values.
# from collections import defaultdict
# clas=["Class V","Class V|","Class V||","Class V|||"]
# num=[1,2,3,3]
# dic=defaultdict(set)
# for i,c in zip(clas,num):
#     dic[i].add(c)
# print(dic)



# Write a Python program to match key values in two dictionaries.
# d1={'key1': 1, 'key2': 3, 'key3': 2}
# d2={'key1': 1, 'key2': 2}
# print(f"{set(d1.items()).intersection(set(d2.items()))} is present in both d1 and d2")



# Write a Python program to store a given dictionary in a json file.
# dic={"students": [{"firstName": "Nikki", "lastName": "Roysden"},
#                   {"firstName": "Mervin", "lastName": "Friedland"},
#                   {"firstName": "Aron ", "lastName": "Wilkins"}],
#      "teachers": [{"firstName": "Amberly", "lastName": "Calico"},
#                   {"firstName": "Regine", "lastName": "Agtarap"}]}
# print("The original dictionary:")
# print(dic)
# import json
# print("Importing json")
# with open("dictionary","w") as f:
#     json.dump(dic,f,indent=3,sort_keys=True)
#
# with open("dictionary") as f:
#     data=json.load(f)
# print(data)



# Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
# dic= {}
# lis=[]
# key=["x","y","z"]
# c=11
# d=20
# for x in range(len(key)):
#     for i in range(c,d):
#         lis.append(i)
#     dic[key[x]]=lis
#     lis=[]
#     c+=10
#     d+=10
# print(dic)
# for i in dic.values():
#     print(i[4])



# Write a Python program to drop empty Items from a given Dictionary.
# dic={"Red":None,"Black":"1","Violet":3,"White":None}
# dic={x:y for (x,y) in dic.items() if y is not None}
# print(dic)



# Write a Python program to filter a dictionary based on values
# dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("Marks greater than 179")
# dic={x:y for (x,y) in dic.items() if y>179}
# print(dic)




