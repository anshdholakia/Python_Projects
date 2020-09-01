
dict1= {"Harry potter 1": "None", "Harry potter 2": "Lewis", "Harry potter 3": "harry", "Harry potter 4": "None",
        "Elon musk":"None"}

class Library:
    def __init__(self,book_name,book_owner):
        self.book_name=book_name
        self.book_owner=book_owner



    def display_book(self):

        for key,value in dict1.items():
            if value=="None":
                return f"The library has:{dict1.keys()}"


    def lend_book(self):
        if self.book_name not in dict1:
            return f"{self.book_name} is not available"
        elif (dict1.get(self.book_name) == "None"):
            dict1.update({self.book_name: self.book_owner})
            return f"You are lending a book called {self.book_name} and was owned by 'no one' and is now owned by '{dict1.get(self.book_name)}'\n"


        elif self.book_owner==dict1.get(self.book_name):
            return "You already have the book. Please check"

        elif(dict1.get(self.book_name)!= "None"):
            return f"This book is owned by {dict1.get(self.book_name)}, please wait until returned"

        else:
            return f"{self.book_name} is not present in the library"


    def return_book(self):
        if (self.book_name in dict1):
            dict1.update({self.book_name:"None"})
            return f"Thank you for returning {self.book_name}"
        else:return "Please check again wrong input"





    def add(self,user):
        self.user=user
        if self.book_name!=dict1.keys():
            dict1.update({self.book_name:"None"})
            return f"Thank you for donating {self.book_name} to our collection, {self.user}\nThis is our updated collection: {dict1.keys()}\n"

        else:
            print("This book is already in our library. Thank you")


print("\t\t\t\t\t\t\t~~~~ Welcome to the Library ~~~~\t\t\t\t\t\t\t\t")

while (True):
    import time
    z=int(input(print("\nEnter\n1 for viewing our library\n2 for lending a book\n3 for returning a book\n4 for donating a book: \n")))
    time.sleep(2)
    if z==1:

        ansh=Library("None","None")
        print(ansh.display_book())
        k = input("Do you want to continue (y/n) : ")
        if k == "y":
            continue
        elif k == "n":
            exit()

    elif z==2:
        b=input("Enter book name:\n")
        c=input("Enter your name:\n")
        ansh=Library(b,c)
        print(ansh.lend_book())
        k = input("Do you want to continue (y/n) : ")
        if k == "y":
            continue
        elif k == "n":
            exit()

    elif z==3:
        b=input("Enter book name:\n")
        c=input("Enter your name:\n")
        ansh=Library(b,c)
        print(ansh.return_book())
        k = input("Do you want to continue (y/n) : ")
        if k == "y":
            continue
        elif k == "n":
            exit()

    elif z==4:
        b = input("Enter book name:\n")
        v = input("Enter your name:\n")
        ansh = Library(b, v)
        print(ansh.add(v))
        k = input("Do you want to continue (y/n) : ")
        if k == "y":
            continue
        elif k == "n":
            exit()




