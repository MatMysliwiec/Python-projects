def mortgage_calculator(loan, interest_rate, terms, compounding_interval):

    if compounding_interval.lower().startswith('m'):
        periods = terms * 12
    elif compounding_interval.lower().startswith('w'):
        periods = terms * 52
    elif compounding_interval.lower().startswith('d'):
        periods = terms * 365
    elif compounding_interval.lower().startswith('c'):
        periods = terms * 365 * 100
    else:
        print("Invalid compounding interval.")
        return

    # Calculate monthly payment using the correct formula
    if interest_rate == 0:
        monthly_payment = loan / periods
    else:
        monthly_interest_rate = interest_rate / 100 / 12
        denominator = (1 - (1 + monthly_interest_rate) ** -periods) / monthly_interest_rate
        monthly_payment = loan / denominator

    total_repayment = monthly_payment * periods

    def change_str_compounding_interval(interval):

        if interval.lower().startswith('m'):
            return "Monthly"
        elif interval.lower().startswith('w'):
            return "Weekly"
        elif interval.lower().startswith('d'):
            return "Daily"
        elif interval.lower().startswith('c'):
            return "Continually"
        else:
            print("Invalid compounding interval.")
            return interval

    print(f"Principal: {loan} zl")
    print(f"Interest Rate: {interest_rate}%")
    print(f"Loan Terms: {int(terms)} years")
    print(f"Compounding Interval: {change_str_compounding_interval(compounding_interval)}")
    print(f"Monthly Payment: {monthly_payment:.2f} zl")
    print(f"Total Repayment: {total_repayment:.2f} zl")


loan = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
terms = float(input("Enter the loan terms in years: "))
compounding_interval = input("Enter the compounding interval (Monthly, Weekly, Daily, Continually): ")

mortgage_calculator(loan, interest_rate, terms, compounding_interval)
