from sympy import symbols, limit, oo


def limit_calculator():
    function_str = input("Enter the function f(x): ")
    limit_value_str = input("Enter the limit value: ")

    x = symbols('x')
    function = eval(function_str)

    if limit_value_str.lower() == 'oo':
        limit_value = oo
    else:
        limit_value = float(limit_value_str)

    result = limit(function, x, limit_value)
    print(f"The limit of {function_str} as a x approaches {limit_value_str} is {result:.2f}")


limit_calculator()