# to count the number of Vowels
text = input("Enter a string: ")
i = 0
for char in range (0,len(text)):
    if text[char] in ('a','e','i','o','u','A','E','I','O','U'):
        i += 1
print(f"Total Vowels = {i}")