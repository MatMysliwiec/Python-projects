def factorial_with_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_with_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_with_recursion(n - 1)

while True:

    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a non-negative integer")
    else:
        result_loop = factorial_with_loop(num)
        result_recursion = factorial_with_recursion(num)
        print(f"Factorial using loop {result_loop}, factorial using recursion {result_recursion}")
        break

