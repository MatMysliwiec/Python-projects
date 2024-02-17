import timeit


def fast_pow(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half_pow = fast_pow(a, b // 2)
        return half_pow * half_pow
    else:
        half_pow = fast_pow(a, (b - 1) // 2)
        return a * half_pow * half_pow


a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))

start1 = timeit.default_timer()
result1 = fast_pow(a, b)
print("Working time function fast_pow: ", timeit.default_timer()-start1)
print(f"Result of fast_pow: {result1}")

start2 = timeit.default_timer()
result2 = pow(a,b)
print("Working time function pow: ", timeit.default_timer()-start2)
print(f"Result of pow: {result2}")