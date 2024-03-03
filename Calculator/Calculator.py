def calculator(arg):
    argument = [arg]

    def arg_collector(arg):
        if arg != '=':
            argument.append(arg)
            return arg_collector

        result = argument[0]

        for operator, operand in zip(argument[1::2], argument[2::2]):
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
            elif operator == "**":
                result **= operand

        return result

    return arg_collector


def test_calculator():
    calc = calculator(5)

    # Test dodawania
    result = calc('+')(3)('=')
    assert result == 8, f"Błąd dla testu 1. Oczekiwano: 8, Otrzymano: {result}"

    # Test odejmowania
    result = calculator(10)('-')(7)('=')
    assert result == 3, f"Błąd dla testu 2. Oczekiwano: 3, Otrzymano: {result}"

    # Test mnożenia
    result = calculator(4)('*')(5)('=')
    assert result == 20, f"Błąd dla testu 3. Oczekiwano: 20, Otrzymano: {result}"

    # Test dzielenia
    result = calculator(15)('/')(3)('=')
    assert result == 5, f"Błąd dla testu 4. Oczekiwano: 5, Otrzymano: {result}"

    # Test potęgowania
    result = calculator(2)('**')(3)('=')
    assert result == 8, f"Błąd dla testu 5. Oczekiwano: 8, Otrzymano: {result}"

    print("Test wykonane pomyślnie")


test_calculator()
