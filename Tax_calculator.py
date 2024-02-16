def is_valid_cost(input_str):
    try:
        cost = float(input_str)
        return cost >= 0
    except ValueError:
        return False


def calculate_pit(cost, deductible_cost):
    if 120000 >= cost > 30000:
        tax = cost * 0.12
        tax = tax - deductible_cost
        total_cost = cost + tax
        return tax, total_cost
    elif cost > 120000:
        Itax = (120000 * 0.12) - deductible_cost
        tax = (cost - 120000.0) * 0.32
        tax = tax + Itax
        total_cost = cost + tax
        return tax, total_cost


try:
    while True:
        cost_str = input("Enter the income: PLN ")
        deductible_cost_str = input("Enter the deductible cost: ")
        if is_valid_cost(cost_str) and is_valid_cost(deductible_cost_str):
            cost = float(cost_str)
            deductible_cost = float(deductible_cost_str)
            break
        else:
            print("Invalid input. Please enter a valid numeric value for the income.")

    pit, total_income = calculate_pit(cost, deductible_cost)

    print(f"\nPersonal Income Tax (PIT): PLN {pit:.2f}")
    print(f"Total income after tax: PLN {total_income:.2f}")

except ValueError:
    print("Please enter a valid numeric value for the income.")
