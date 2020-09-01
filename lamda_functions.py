#lamda functions or anonymous functions used to make a fucntion
# def add(a,b):
#     return a+b
# THIS IS THE OLD STYLE METHOD
# print(add(333,0))

#example

# add= lambda x,y: x+y
#
# print(add(3,4))
# def a_first(a):
#     return a[1]
#
# a=[[1,7],[3,4],[5,8]]
# a.sort(key=a_first) #sort arranges
# print(a)

# other method with defining function through lambda function
a=[[1,7],[3,4],[5,8]]
a.sort(key= lambda x:x[1]) #sort arranges
print(a)
