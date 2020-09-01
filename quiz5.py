import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("lewis-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("lewis-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("shaw-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("shaw-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("ansh-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("ansh-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(lewis),2(shaw),3(ansh)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("lewis-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("lewis-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("shaw-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("shaw-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("ansh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("ansh-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (lewis,shaw,ansh)")
print("health management system: ")

a=int(input("press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for lewis 2 for shaw 3 for ansh "))
    take(b)
else:
    b = int(input("press 1 for lewis 2 for shaw 3 for ansh "))
    retrieve(b)