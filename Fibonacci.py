def fibonacci(n):
    if n == 1:
        return [1,0]
    else:
        digit = fibonacci(n-1)
        digit = [digit[0] + digit[1], digit[0]]
        return digit

def validate():

    while True:
        s = input("Number to generate fibonacci sequence: ")
        try:
            digits = int(s)
            if digits > 0:
                return digits
            else:
                print("Enter a nonnegative integer.")
        except ValueError:
            print("Enter a nonnegative integer.")

Digits = validate()
print("Result: ", fibonacci(Digits)[0])