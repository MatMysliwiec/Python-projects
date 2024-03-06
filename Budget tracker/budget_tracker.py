from datetime import datetime, timedelta
from abc import ABC


class Transaction(ABC):
    def __init__(self, amount, description, date):
        self.amount = amount
        self.description = description
        self.date = date


class Income(Transaction):
    def __str__(self):
        return f"Income +${self.amount} ({self.date}): {self.description}"


class Expense(Transaction):
    def __str__(self):
        return f"Expense: -${self.amount} ({self.date}): {self.description}"


class RecurringCost(Transaction):
    def __init__(self, amount, description, start_date, end_date, frequency):
        super().__init__(amount, description, start_date)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __str__(self):
        return f"Recurring Cost: -${self.amount} ({self.start_date} to {self.end_date}, {self.frequency}): {self.frequency}"


class BudgetTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.recurring_costs = []

    def add_income(self, amount, description, date):
        income = Income(amount, description, date)
        self.incomes.append(income)

    def add_expense(self, amount, description, date):
        expense = Expense(amount, description, date)
        self.expenses.append(expense)

    def add_recurring_cost(self, amount, description, start_date, end_date, frequency):
        recurring_cost = RecurringCost(amount, description, start_date, end_date, frequency)
        self.recurring_costs.append(recurring_cost)

    def calculate_net_flow(self, start_date, end_date):
        net_flow = 0
        for income in self.incomes:
            if start_date <= income.date <= end_date:
                net_flow += income.amount

        for expense in self.expenses:
            if start_date <= expense.date <= end_date:
                net_flow -= expense.amount

        for recurring_cost in self.recurring_costs:
            current_date = recurring_cost.start_date
            while current_date <= end_date:
                if start_date <= current_date <= end_date:
                    net_flow -= recurring_cost.amount
                current_date += timedelta(days=recurring_cost.frequency)

        return net_flow

    def display_transactions(self):
        all_transactions = self.incomes + self.expenses + self.recurring_costs
        all_transactions.sort(key=lambda x: x.date)

        for transaction in all_transactions:
            print(transaction)


budget_tracker = BudgetTracker()

budget_tracker.add_income(3000, "Salary", datetime(2024, 3, 1))
budget_tracker.add_expense(1000, "Rent", datetime(2024, 3, 5))
budget_tracker.add_recurring_cost(50, "Subscription", datetime(2024, 3, 2), datetime(2024, 3, 31), 7)

budget_tracker.display_transactions()

start_date = datetime(2024, 3, 1)
end_date = datetime(2024, 3, 31)
net_flow = budget_tracker.calculate_net_flow(start_date, end_date)
print(f"\nNet Flow from {start_date} to {end_date}: ${net_flow}")
