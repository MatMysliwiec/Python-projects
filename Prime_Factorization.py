from math import isqrt


def trial_division(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


n = int(input("Number to find its prime factors: "))
factors = []
while True:
    if n == 0 or n == 1:
        break

    for i in range(2, n + 1):
        if n % i == 0:
            if trial_division(i):
                factors.append(i)
                n //= i
                break

if len(factors) != 0:
    factors = [str(factor) for factor in factors]
    print(', '.join(factors))
else:
    print("Number", n, "doesn't have any prime number")
