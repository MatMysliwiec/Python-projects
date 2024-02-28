import sys
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


def generator(current: int):
    new = current + 1
    while True:
        if not trial_division(new):
            new += 1
        else:
            break

    return new


currentPrime = 2
while True:
    counts = input("Would you like to generate another prime number, press enter. To exit press esc) ")
    try:
        if counts.lower() == '':
            print(currentPrime, end="\n")
            currentPrime = generator(currentPrime)
        elif counts.lower() == 'q':
            break
    except ValueError:
        print("Try again", end="\n")
