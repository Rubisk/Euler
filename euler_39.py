def get_triangle_sides(maximum):
    maximum_p = (0, 0)
    for p in range(2, maximum):
        if p % 100 == 0:
            print p
        l = 0
        for c in range(1, p):
            c2 = c * c
            bs = []
            for a in range(1, (p - c)):
                if a in bs:
                    continue
                b2 = c2 - a * a
                if b2 <= 0:
                    continue
                b = p - a - c
                if a * a + b * b == c * c:
                    bs.append(int(b))
                    l += 1
        if l > maximum_p[1]:
            maximum_p = p, l
    return maximum_p[0]


if __name__ == "__main__":
    print get_triangle_sides(1000)