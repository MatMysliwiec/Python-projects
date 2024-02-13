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
    koniec = input("Would you like to generate another prime number? y/n: ")
    if koniec.lower().startswith('y'):
        print(currentPrime, end="\n")
        currentPrime = generator(currentPrime)
    elif koniec.lower().startswith('n'):
        break
    else:
        print("Try again", end="\n")
