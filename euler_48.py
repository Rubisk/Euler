sum = 0

for i in range(1, 1001):
    p = i
    for n in range(i - 1):
        p *= i
        p %= 100000000000
    sum += p
    sum %= 100000000000

print sum