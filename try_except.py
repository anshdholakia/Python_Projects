print("Enter a number 1")
num1=input()
print("Enter a number 2")
num2=input()
try:                                                                  # Due to try and except the program showed error but also
    print("The sum of these two numbers is:", int(num1) + int(num2))  # print the code "ynamaha" after it.
except Exception as e:   # we handle this exception(the inputs are strings) by putting a try-except.
    print(e)

print("Ynamaha") # this line wont print as error will show before it when I type a string in the input instead of an integer.