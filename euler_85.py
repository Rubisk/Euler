import sys


def find_rectangle_closest_to(rectangles):
    rectangles *= 4
    n = 1
    n_product = 2
    closest = (rectangles, 0, 0)
    while n_product < rectangles:
        m = 1
        m_product = 2
        while m <= n:
            if abs(rectangles - n_product * m_product) < closest[0]:
                closest = abs(rectangles - n_product * m_product), m, n
            m += 1
            if m >= 2:
                m_product /= (m - 1)
            m_product *= (m + 1)
        n += 1
        if n >= 2:
            n_product /= (n - 1)
        n_product *= (n + 1)
    return closest[1], closest[2]


if __name__ == "__main__":
    print find_rectangle_closest_to(int(sys.argv[-1]))
