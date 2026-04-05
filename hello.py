name = input("Enter your name: ")
print(f"Hello {name}! Welcome to my GitHub!")
#Celcius to Fahrenheit
cel = int(input("Enter the temperature in celsius: "))
fahh = (9/5)*cel + 32
print(fahh)

#simple intrest calculator
p = int(input("Enter the principle amount: "))
t = int(input("Enter the time period in yrs: "))
r = int(input("Enter the rate of intrest: "))

SI = (p*t*r)/100
print(SI)
print(f"Total intrest you got is {SI}, the total amount you have now is {SI + p}")

#swapping two numbers
x = int(input("Enter x: "))
y = int(input("Enter y: "))

x,y = y,x
print(x)
print(y)

#To check odd or even
n = int(input("Enter the number: "))

if n%2 == 0:
    print("Even")
else:
    print("Odd")
