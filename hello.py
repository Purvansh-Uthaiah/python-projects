n = int(input("Enter ho many terms you want: "))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Invalid! Please enter a positive integer")
elif n == 1:
    print("The fibonacci sequence upto ", n1 )
    print(n1)
else:
    print("The fibonacci sequence is: ")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        

