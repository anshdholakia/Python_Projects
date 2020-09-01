# numbers=["1","2","3"]
#
# # for i in range(len(numbers)): # not suitable every-time to use a for loop
# #     numbers[i]=int(numbers[i])
#
# # using a map function
# numbers=list(map(int,numbers))
#
#
# numbers[2]=numbers[2]+5
#
# print(numbers[2])

# def sq(a):
#     return a*a
# num=[1,2,124,4,5,5,123,23,3,53]
# square=list(map(sq, num))
# print(square)

#
#
#
# num=[1,2,124,4,5,5,123,23,3,53]
# square=list(map(lambda x:x*x, num))
# print(square)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# function=[square,cube]
#
# for i in range(6): #[0,6)
#     func=list(map(lambda x:x(i),function ))
#     print(func)

######################################## FILTER ########################################################

#FILTER FUNCTION
# It makes a list of elements on which the given function is true


# list_1=[1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5
#
# # gr_than_5=filter(is_greater_5,list_1) this will give you a filter variable
# # print(gr_than_5)
# gr_than_5=list(filter(is_greater_5,list_1))
# print(gr_than_5)



######################################## REDUCE #############################################################3
from functools import reduce
list1=[1,2,3,4]  # how to add all the numbers in the list
num=reduce(lambda x,i:x+i, list1)
print(num)
