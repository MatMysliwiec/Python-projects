def number_to_words(num):
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative " + number_to_words(abs(num))

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def below_hundred(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        else:
            return tens[n // 10] + " " + units[n % 10]

    result = ""
    if num // 1000 > 0:
        result += number_to_words(num // 1000) + " Thousand "
        num %= 1000
    if num // 100 > 0:
        result += units[num // 100] + " Hundred "
        num %= 100
    if num > 0:
        result += below_hundred(num)

    return result.strip()


while True:
    try:
        num = int(input("Enter a number: "))
        if 0 <= abs(num) <= 1000000:
            result = number_to_words(num)
            print(f"Number in words: {result}")
        else:
            print("Please enter a integer up to one milion")
        end = input("Want to continue (y/n): ")
        if end.lower().startswith("n"):
            break
        else:
            continue
    except ValueError:
        print("Invalid input.")
