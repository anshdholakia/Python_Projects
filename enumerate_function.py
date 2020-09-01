lst=["bhindi","potato","chopsticks","rasgulla"]
#
# i=1
# for item in lst:
#     if i%2!=0:
#         print(f"hiro, please buy {item}")
#     i+=1


for index, item in enumerate(lst):  #it gives index number as well as item name
    if index%2==0:
        print(f"hiro, please buy {item}\n")