def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


print("Select operation to perform :"
      "\n1.Addition "
      "\n2.Subtraction"
      "\n3.Multiplication"
      "\n4.Division")


while True:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    op = int(input("Enter operation option :"))
    if op == 1:
        print(add(a, b))

    if op == 2:
        print(sub(a, b))

    if op == 3:
        print(mul(a, b))

    if op == 4:
        try:
            print(div(a, b))
        except ZeroDivisionError:
            print("You cannot divide a number by zero")
    if op not in (1, 2, 3, 4):
        print("Enter correct operation action")
