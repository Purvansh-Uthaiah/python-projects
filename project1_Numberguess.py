import random
print("Welcome to the number guessing game ! Let's get Started")

num = random.randint(1, 100)

i = 0
Guess = int(input("Enter your number: "))

while Guess != num:
    if (Guess < num):
        print("Too Low!, Go higher... ")
        i += 1
        Guess = int(input("Enter you guess again: "))


    elif (Guess > num):
        print("Too High!,Go lower... ")
        Guess = int(input("Enter your guess again: "))
        i += 1

else:
    print(f"Got it! Hurray!!!, you Guessed the number in {i} trials")


