#largest of the three numbers without using max()

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

if (a>b and a>c):
    print("Greatest number is",a)
elif(b>a and b>c):
    print("Greatest number is",b)
else:
    print("Greatest number is",c)