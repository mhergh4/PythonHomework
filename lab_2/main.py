from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        common_factor = gcd(numerator, denominator)
        self.numerator = numerator // common_factor
        self.denominator = denominator // common_factor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

if __name__ == "__main__":
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)

    print("Fraction 1:", fraction1)
    print("Fraction 2:", fraction2)

    sum_fraction = fraction1 + fraction2
    print("Sum:", sum_fraction)

    difference_fraction = fraction1 - fraction2
    print("Difference:", difference_fraction)

    product_fraction = fraction1 * fraction2
    print("Product:", product_fraction)

    quotient_fraction = fraction1 / fraction2
    print("Quotient:", quotient_fraction)
