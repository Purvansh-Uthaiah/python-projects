# A Simple Calculator

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def prod(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b


while True:
    print("1-> To Add")
    print("2-> To Subtract")
    print("3-> To Multiply")
    print("4-> To Divide")
    print("5-> To Exit")

    choice = int(input("Choose your operation: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(add(a, b))


    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(sub(a, b))


    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(prod(a, b))


    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(div(a, b))


    else:
        print("Thankyou ,Goodbye")
        break