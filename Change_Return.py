def change_calc(cost, amount):
    change = amount - cost
    if change < 0.0:
        print("Not enough money given to cover the cost")
        return
    change_in_cents = int(change * 100)
    quarters = change_in_cents // 25
    dimes = (change_in_cents % 25) // 10
    nickels = ((change_in_cents % 25) % 10) // 5
    pennies = ((change_in_cents % 25) % 10) % 5

    print("\nChange:")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

    return quarters, dimes, nickels, pennies


Amount = input("Amount of money given: ")
Cost = input("Cost: ")
change_calc(float(Cost), float(Amount))
