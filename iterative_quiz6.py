def fibo(n):
    """

    :param n:
    :return:
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2)) #recursion

number=int(input("Enter any number\n"))
print(fibo(number))