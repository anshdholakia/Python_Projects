s=set([1, 2, 3, 4])
#print(type(s))
#set1=set(s)
#print(set1)
s.add(1)
#s.union({1,2,3,5}) # this statment does not do anything as it only specifies the union but does not implement it
#It only implements when it is STORED IN ANOTHER SET such as s1
#s1= s.union({1,2,3,5})
#s1= s.intersection({1,3,4,5,6})
#print(s, s1)
#how to check disjoint function (boolean type)
ss1=([5,6])
print(s.isdisjoint(ss1))
#https://www.w3schools.com/python/python_ref_set.asp