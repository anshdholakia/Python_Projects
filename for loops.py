#list1=["Ansh", "Srinivas", "Hriday", "Siddharth"]
#print(list1[0], list1[1]) # for printing numerous items use this method down below
list1=[["Chocolate",1], ["Sweets",4], ["willy wonka", 2]] # it will print a list in the list for this type of list
#for item, quantity in list1: # : is an indentation that is necessary for elif else if and for loops
 # print(item, quantity) # it repeats for all elements
dict1=dict(list1)
#print(dict1)
#for item,quantity in dict1.items():
 #   print(item, quantity) # error without .items()

#for item in dict1: # only to print keys
 #   print(item)
random_items=[34,334,232,"ansh",33,23,4,2,3,1]

for item in random_items:
    if str(item).isnumeric() and item>23: # write numeric in str type as it will typecast in in string form
        print(item)