class Rational:
    def __init__(self, numerator=1, denominator=2):
        from math import gcd

        if type(numerator) is not int or type(denominator) is not int:
            raise Exception('Invalid value')

        self.numerator = int(numerator / gcd(numerator, denominator))
        self.denominator = int(denominator / gcd(numerator, denominator))  

    def print_frac(self):
        print(self.numerator, '/', self.denominator, sep='')

    def print_float(self):
        print(self.numerator / self.denominator)

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)
