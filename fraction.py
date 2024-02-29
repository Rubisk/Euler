class Fraction(object):
    auto_simplify = True
    _n = 1
    _d = 1

    def __init__(self, n, d=1):
        self.numerator = n
        self.denominator = d

    @property
    def numerator(self):
        return self._n

    @property
    def denominator(self):
        return self._d

    @numerator.setter
    def numerator(self, n):
        self._n = n
        if self.auto_simplify:
            self.simplify()

    @denominator.setter
    def denominator(self, d):
        if d == 0:
            raise ZeroDivisionError
        self._d = d
        if self.auto_simplify:
            self.simplify()

    def __mul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def simplify(self):
        g = ggd(self.numerator, self.denominator)
        self._n /= g
        self._d /= g

    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        a, b = self.numerator, self.denominator
        c, d = other.numerator, other.denominator
        return Fraction(a * d + b * c, b * d)

    def __radd__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        a, b = self.numerator, self.denominator
        c, d = other.numerator, other.denominator
        return Fraction(a * d + b * c, b * d)

    def __repr__(self):
        return str(self.numerator) + " / " + str(self.denominator)

    def __cmp__(self, other):
        if other is None:
            return -1
        return cmp(self.numerator * other.denominator, self.denominator * other.numerator)

def test_fraction():
    assert Fraction(2, 3) + Fraction(1, 3) == Fraction(1, 1)
    assert Fraction(4, 12) * Fraction(2, 12) == Fraction(8, 144)
    assert 2 * Fraction(3, 7) == Fraction(6, 7)
    assert str(Fraction(8, 144)) == "1 / 18"

