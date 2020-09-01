#print list containing numbers divisible by 3

# ls=[i for i in range(100) if i%3==0]
# print(ls)


#Dict comprehension
# dict1={i:f"item{i}" for i in range(100)}
# dict1={value:key for key,value in dict1.items()} # it will get reversed
# print(dict1)


#Set comprehension
# dress={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dress)

#generator type comprehension
# evens=(i for i in range(100) if i%2==0)
# print(type(evens))  # It is a generator type as it is YIELDING values
# # print(evens)
# # print(evens.__next__())
# for item in evens:
#     print(item)


# little exercise

a=int(input("Enter the number of items you want\n"))
b=int(input("Enter 1 for list, 2 for dict, 3 for set\n"))

list1=[i for i in range(a) if b==1]
print(list1)

dict1={i:f"item{i}" for i in range(a) if b==2}
print(dict1)


set1={i for i in range(a) if b==3}
print(set1)