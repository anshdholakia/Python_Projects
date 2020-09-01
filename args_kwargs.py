# def function_name(a,b,c,d,e):
#     print(a,b,c,d,e)
# function_name("ansh", "harry", "messi", "pavard", "roger")
# advantage of args- the things you add in list you wont have to update function
#
# def name(statement,*args): #have to place *args in the last argument
#     print(statemen)
#     for items in lst:
#      print(items)
# lst=["ansh", "harry", "messi", "vikk", "tobi", "delle", "debruyne", "dejong"]
# statemen="hello these are the names of some famous footballers:"
# name(statemen, *lst)

#new
def name(statement,*args, **kwargsch): #have to place *args in the 2nd last argument and **kwargs in the last
    print(statemen)
    for items in lst:
     print(items)
    for names,values in kwargsch.items():
        print(f"{names} is a {values}")
lst=["ansh", "harry", "messi", "vikk", "delle", "debruyne", "dejong"]
statemen="hello these are the names of some famous footballers:"
kw={"Ansh":"manager","messi":"goat","ronaldo":"diver","phil foden":"prodigy"}
name(statemen, *lst, **kw)

