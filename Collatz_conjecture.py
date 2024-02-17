def collatz(n):
    k = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        k += 1
    return k


try:
    number = int(input("Enter a number greater than 1: "))
    if number > 1:
        steps = collatz(number)
        print(f"Number of steps to reach 1: {steps}")
    else:
        print("Please enter a number greater than 1")
except ValueError:
    print("invalid input")
