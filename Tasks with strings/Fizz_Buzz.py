def FizzBuzz():
    numbers = [i for i in range(1, 101)]
    for i in range(1, len(numbers)):
        if (numbers[i] % 3 == 0) and (numbers[i] % 5 == 0):
            numbers[i] = "FizzBuzz"
        elif numbers[i] % 5 == 0:
            numbers[i] = "Buzz"
        elif numbers[i] % 3 == 0:
            numbers[i] = "Fizz"

    print(numbers)


FizzBuzz()