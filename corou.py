############# COROUTINE ################

def search_book():
    import time
    book="This is a book or harry kane and raheem sterling"
    # Some task consuming 4 seconds
    time.sleep(4)


    while True:
        text=(yield)

        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")


search=search_book()
next(search)  # coroutine is starting
search.send("harry")
input("Press any key")
search.send("and")  #this operation will not take 4 additonal seconds as the text is yielded and
# it will start from the while loop


search.close() #this stops the coroutine
# search.send("eeee") #Stop iteration error after coroutine is closed.




#SmallExercise

def searchinfile():
    import time
    f=open("1.txt")
    w=f.read()
    time.sleep(4)

    while True:
        text=(yield)
        if text in w:
            print("Your name is in the file")
        else:
            print("Your name is not in the file")


search=searchinfile()
next(search)
while True:
    search.send(input("Enter your name"))

