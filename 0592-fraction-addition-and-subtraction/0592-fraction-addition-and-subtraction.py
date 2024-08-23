class Solution:
    def fractionAddition(self, expression: str) -> str:

        fractions = re.findall('[+-]?\d+/\d+', expression)

        numerator = 0
        denominator = 1
        

        for frac in fractions:
            num, den = map(int, frac.split('/'))

            numerator = numerator * den + num * denominator
            denominator *= den
            
            common = gcd(abs(numerator), denominator)
            numerator //= common
            denominator //= common

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        return f"{numerator}/{denominator}"