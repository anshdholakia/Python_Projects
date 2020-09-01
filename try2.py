f1=open("ansh.txt")

try:
    f=open("dsf.txt")

# except Exception as e:
#     print(e)

except EOFError as e:               # EOF - End of File
    print("EOF Error occured",e)

except IOError as e:                # IO - Input Operation
    print("IO Error has occured",e)

else:
    print("This will run only if except is not running")


finally:   #finally is used to excecute a code that should run anyways
    print("Closing file")
    f1.close()

print("Code has run")
