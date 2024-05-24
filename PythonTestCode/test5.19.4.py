def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numerator, denominator = map(int, input().split())

common_factor = gcd(numerator, denominator)
numerator //= common_factor
denominator //= common_factor

print(numerator, denominator)
