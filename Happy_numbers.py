"""A happy number is defined by the following process. Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers."""


def is_happy_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def find_happy_numbers(count):
    happy_numbers = []
    number = 1
    while len(happy_numbers) < count:
        if is_happy_number(number):
            happy_numbers.append(number)
        number += 1
    return happy_numbers


counts = 9
print(f"First {counts} happy numbers are: ", find_happy_numbers(counts))
