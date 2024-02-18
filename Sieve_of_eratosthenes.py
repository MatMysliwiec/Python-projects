def Sieve_of_Eratosthenes(n):
    if n < 2:
        return print("Invalid input. Enter integer greater than 2.")
    prime = [True for i in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [num for num in range(2, n + 1) if prime[num]]


limit = int(input("Enter the limit for finding primes: "))
result = Sieve_of_Eratosthenes(limit)
print("Prime numbers up to", limit, "are", ", ".join(map(str, result)))
