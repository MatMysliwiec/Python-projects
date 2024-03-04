from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hourly_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hourly_worked


class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_pay(self):
        return self.salary


class Manager(SalariedEmployee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus


class Executive(Manager):
    def __init__(self, name, employee_id, salary, bonus, stock_option):
        super().__init__(name, employee_id, salary, bonus)
        self.stock_option = stock_option

    def calculate_pay(self):
        return super().calculate_pay() + self.stock_option


class Company:
    def __init__(self):
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} (ID: {employee.employee_id}) has been hired.")

    def fire_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print(f"{employee.name} (ID:{employee.employee_id} has been fired")
                return
            print(f"No employee found with ID {employee.employee_id}")

    def raise_employee(self, employee_id, raise_amount):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                if isinstance(employee, HourlyEmployee):
                    print(f"Hourly employee cannot receive raises")
                else:
                    if isinstance(employee, Executive):
                        print("Executives receive raises through stock options.")
                    else:
                        employee.salary += raise_amount
                        print(f"{employee.name} (ID: {employee.employee_id}) has received a raise of ${raise_amount}.")
                    return
                print(f"No employee found with ID {employee_id}.")
