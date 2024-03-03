def valid_credit_card(number):
    card_digit = [int(digit) for digit in number.replace(" ", "")]
    if len(card_digit) != 16:
        return False

    sum1 = 0
    sum2 = 0
    sum3 = 0

    for i in range(0, 15, 2):
        sum1 += card_digit[i]
    sum1 *= 2

    for i in range(1, 15, 2):
        sum2 += card_digit[i]

    for i in range(0, 15, 2):
        if card_digit[i] > 4:
            sum3 += 1

    checksum = sum1 + sum2 + sum3

    check_digit = 10 - (checksum % 10)

    if card_digit[15] == check_digit:
        return True
    else:
        return False


card_number = input("Enter the credit card number: ")

if valid_credit_card(card_number):
    print("The credit card number is valid.")
else:
    print("Invalid credit card number.")
