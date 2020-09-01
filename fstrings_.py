#F strings
# d="ansh"
# s="dholakia"
# p="this is %s"%d # d got inserted into s
# m="this is %s %s"%(d,s) # d got inserted into s
# print(m,"\n")
# print(p,"\n")

# a= "this is {1} {0}"
# b=a.format("dholakia", "ansh") # as dholakia's index is at 0 and ansh's at 1
# print(b)
import math


n="ansh"
s="dholakia"


# f string method
a=f"This is {n} {s} {math.sqrt(25)}"
print(a)