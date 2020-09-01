
def statement(str):
    return f"Give this string to ansh{str}"

def add(num1, num2):
    return num1+num2+5

print("and the name is",__name__)
# if I run tutmain2.py it will also print these lines, hence to skip it we use __name__='__main__'
if __name__=='__main__':
    print(statement("dholakia"))
    print(add(5,4))