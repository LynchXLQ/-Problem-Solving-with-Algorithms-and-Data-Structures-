# Time: 2021/11/4  20:17
class Fraction:
    def __init__(self,top, bottom):
        self.numerator = top
        self.denominator = bottom

    def show(self):
        print(self.numerator, '/', self.denominator)

    def gcd(self, a, b):   # greatest common divisor，GCD
        while a%b != 0:
            old_a = a
            old_b = b
            a = old_b
            b = old_a%old_b
        return b

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __eq__(self, other:'Fraction'):
        new_numerator = self.numerator*other.denominator
        new_denominator = self.denominator*other.numerator
        return new_denominator==new_numerator

    def __add__(self, other:'Fraction'):
        new_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        common = self.gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)



f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
f3.show()
