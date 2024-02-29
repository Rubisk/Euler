numbers = []


def powers(a, b):
    if b == 1:
        return a
    else:
        return a * powers(a, b - 1)


for i in range(2, 101):
    print i
    for j in range(2, 101):
        p = powers(i, j)
        if p not in numbers:
            numbers.append(p)


print len(numbers)
