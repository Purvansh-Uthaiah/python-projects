# multiplication table
n = int(input("Enter a number: "))
i = 0
for char in range (1,11):
    print(f"{n} x {i} = {n*i}")
    i += 1