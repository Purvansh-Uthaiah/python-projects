# sum of numbers from 1 to N without using sum()

def addn(n):
    if n< 1:
        return 0
    else:
        return n + addn(n-1)

print(addn(1))
print(addn(8))
print(addn(9))