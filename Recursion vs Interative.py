#Iterative Example
# factorial example
def factorial_iterative(n):
    """

    :param n: Integer
    :return: i*(i+1)....
    """
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

def factorial_recursive(n):
    """

    :param n: Integer
    :return: i*(i+1)....
    """
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1) # as the function is calling itself it is recursive
number=int(input("Enter a number\n"))
print(factorial_iterative(number))
print(factorial_recursive(number))
