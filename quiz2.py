#faulty calculator

inpopr=str(input("Enter the operator you want to use:"))

int1=int(input("Enter the first number:"))

int2=int(input("Enter the second number:"))

b=inpopr.capitalize()

if b=="Addition" :
    if int1 == 56 and int2 == 9:
        print(77)
    else:
        print(int1+int2)

elif b=="Subtraction":
    print(int1-int2)

elif b=="Multiplication":
    if int1 == 45 and int2 == 3:
        print(555)
    else:
        print(int1*int2)

elif b=="Division":
    if int1 == 56 and int2 == 6:
        print(4)
    else:
        print(int1/int2)


else:
    print("Please try again")


