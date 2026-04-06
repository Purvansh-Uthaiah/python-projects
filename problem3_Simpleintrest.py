p = int(input("Enter the principle amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of intrest: "))

SI = (p*t*r)/100
print(SI)
print(f"Total intrest you got is {SI},the total amount you have now is {SI + p}")
