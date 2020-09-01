#d1={} #{} bracket for dictionary type

#print(type(d1))
d2={"Ansh":"roti", "rohan":"chicken", "sam":"Paneer", "harry":{"B":"burger", "L":"donuts", "D":"Popcorn"}}
#print(d2["harry"]["B"])

# How one can add items
#d2["Ankit"]="Junkfood"
#d2["hriday"]="khakra"
#print(d2)

# how to delete a item from list
# del d2["Ansh"]
# print(d2)

# 1st function of a dictionary- copy
#print(d2.copy())
#d3=d2 # d3 acts as a pointer
#d3=d2.copy() # to remove this error of removing ansh from d2 as well we use copy function
#del d3["Ansh"]
#print(d2)
# ansh got removed from d2 as well because d3 is a POINTER, it does not copy a new list into itself.

# 2nd type function
# get function
#print(d2.get("Ansh"))

#3rd function
#updating list
#d2.update({"leroy":"Healthy food"})
#print(d2)

# 4th type-keys(name printing)
# print(d2.keys())
#5th type-items
#print(d2.items())

