

def ggd(a, b):
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)

total = 0

for b in range(1, 12001):
    if b % 120 == 0:
        print total, b
    a = (b / 3) + 1.
    while a < ((b + 1) / 2):
        if ggd(a, b) == 1:
            total += 1
        a += 1
print total
