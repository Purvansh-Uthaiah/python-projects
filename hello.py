# multiplication table
n = int(input("Enter the number you want: "))
i = 0
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    i += 1