'''
two number
two number should be
+
-
*
/

'''


def add(a, b):
    num = a+b
    print(num)


def subtract(a, b):
    num = a-b
    print(num)


def multiply(a, b):
    num = a*b
    print(num)


def divide(a, b):
    num = a/b
    print(num)


while True:

    a = int(input("enter number"))
    process = input("add/subbtract/multiply/divide")
    b = int(input("enter number"))
    if process == "+":
        add(a, b)
    elif process == "-":
        subtract(a, b)
    elif process == "*":
        multiply(a, b)
    elif process == "/":
        divide(a, b)
