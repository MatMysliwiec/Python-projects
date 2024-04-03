# List of made python projects

## Algorithms

### Closest pair problem

Program to find the smallest distance between two points among a set of given points. The project utilizes a divide and conquer approach to efficiently solve the problem. It calculates the distance between all pairs of points using a brute-force method for small input sizes and optimizes for larger input sizes using a recursive algorithm based on the closest pair of points.

### Collatz conjecture

Collatz conjecture, also known as the 3n + 1 problem. The Collatz conjecture is a sequence defined for positive integers:

1. Start with any positive integer n.
2. If n is even, divide it by 2 (n/2).
3. If n is odd, triple it and add 1 (3n + 1).
4. Repeat the process indefinitely.

### Dijkstra's algorithm

The usage of Dijkstra's algorithm for finding the shortest paths. Implements Dijkstra's algorithm using the NetworkX library. It takes a graph represented as a dictionary of dictionaries where the outer dictionary keys represent nodes, and the inner dictionaries represent neighboring nodes with corresponding edge weights.

### Gauss 3(6) adaptive method

Script provides implementations of adaptive numerical integration methods, particularly the Gauss 3(6)-point adaptive quadrature, to approximate definite integrals of given functions over specified intervals. Implements the adaptive quadrature method using the Gauss 3-point rule. It recursively subdivides the integration interval until a specified tolerance level is achieved, adjusting the step size accordingly.

### Sieve of eratosthenes

The Sieve of Eratosthenes algorithm, an efficient method for finding all prime numbers up to a specified limit. The script takes an integer input representing the upper limit and returns a list of prime numbers within that limit.

### Sorting

Code defines two sorting algorithms: merge sort and bubble sort. It then applies both algorithms to the same array and prints the sorted arrays for comparison.

#### Merge Sort:

Merge sort is a divide-and-conquer algorithm that divides the array into smaller sub-arrays, sorts them recursively, and then merges them back together. It has a time complexity of O(n log n) in the average and worst cases.
#### Bubble Sort:

Bubble sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. It has a time complexity of O(n^2) in the average and worst cases.

## Bandwidth monitor

The provided code is a Python script that monitors network bandwidth usage (upload and download) over a specified duration using the psutil library for system monitoring and matplotlib for visualization. Takes a duration (in minutes) as input and continuously monitors network bandwidth usage for the specified duration. It collects timestamps along with upload and download data at regular intervals using psutil. It updates the user with the time remaining during the monitoring process.
Returns the collected data as lists of timestamps, upload data, and download data.

### Future plans
- [ ] Implement robust error handling to gracefully handle exceptions and invalid user inputs.
- [ ] Optimize the code for better performance, especially if monitoring bandwidth over longer durations or on systems with limited resources. Look for opportunities to reduce unnecessary computations or improve algorithm efficiency.
- [ ] Explore different visualization techniques or libraries to present the network usage data more effectively. Consider adding additional information to the plot, such as labels, annotations, or summary statistics.
- [ ] Extend the functionality to support real-time monitoring of network bandwidth usage, allowing users to see live updates as they occur. This may involve implementing multithreading or asynchronous processing to continuously collect and display data.
- [ ] Develop a graphical user interface (GUI) to provide a more user-friendly experience. This can include interactive features, customization options, and intuitive controls.
- [ ] Ensure that the project is compatible with different operating systems and environments.

## Bank account

Project implements a simple banking system with different types of accounts: CheckingAccount, SavingsAccount, and BusinessAccount. Each account type inherits from the abstract base class Account, defining methods for depositing, withdrawing, and displaying balances.

- Account (Abstract Base Class): Represents the common attributes and methods for all account types. Defines abstract methods for depositing and withdrawing funds, ensuring implementation by subclasses.
- CheckingAccount: Inherits from Account and represents a checking account. Allows depositing and withdrawing funds, with an overdraft limit to prevent overdrawing.
- SavingsAccount: Inherits from Account and represents a savings account. Supports depositing, withdrawing, and adding interest to the balance based on an interest rate.
- BusinessAccount: Inherits from Account and represents a business account. Enables depositing and withdrawing funds, with a transaction fee applied for withdrawals.

### Future plans
- [ ] Implement error handling mechanisms to handle edge cases such as invalid input values (e.g., negative deposit/withdrawal amounts), ensuring that the system remains robust and secure.
- [ ] Implement transaction logging functionality to keep track of all deposit, withdrawal, and interest transactions. This provides an audit trail for account activities and enhances transparency.
- [ ] Implement additional functionality for account management, such as closing an account, transferring funds between accounts, or updating account details (e.g., changing overdraft limits for checking accounts).
- [ ] Enhance the interest calculation mechanism to support different interest compounding frequencies (e.g., monthly, quarterly) and to apply compounding interest rather than simple interest.
- [ ] Develop a simple user interface (e.g., command-line interface or graphical interface) to interact with the banking system, allowing users to perform operations such as depositing, withdrawing, and checking balances more intuitively.
- [ ] Implement localization support to make the system accessible to users from different regions by providing translations for messages and formatting numbers and dates according to local conventions.
- [ ] Enhance security measures, such as implementing authentication mechanisms (e.g., username/password), encryption for sensitive data (e.g., account balances), and protection against common security threats (e.g., SQL injection, cross-site scripting).

## Binary to Decimal converter

Project implements a simple Binary to Decimal and Decimal to Binary converter using the tkinter library for creating a graphical user interface.

The main window of the application displays the title "Binary to Decimal Converter" and provides buttons for converting binary to decimal and decimal to binary. Users can input either a binary or decimal number in the entry field and click the corresponding button to convert it to the other base. Provides immediate feedback to users upon conversion, displaying the result in the respective entry field. Implements error handling to handle invalid input cases, displaying an error message if necessary.

### Future plans

- [ ] Extend input validation to handle more edge cases, such as checking for leading/trailing whitespace, ensuring the entered binary number contains only 0s and 1s, and verifying that the decimal input consists of numeric characters only.
- [ ] Allow users to input numbers using keyboard events (e.g., pressing Enter to trigger the conversion) for improved usability and accessibility.
- [ ] Extend the converter to support larger numbers or implementing custom logic to handle overflow conditions gracefully.
- [ ] Add functionality to allow users to copy the conversion result to the clipboard with a single click, making it easier to use the converted value in other applications.
- [ ] Improve the visual appearance of the GUI by refining the layout, adjusting spacing, and incorporating styling elements (e.g., icons, borders) to enhance the overall aesthetics.

## Blackjack

Python project is a simplified implementation of the classic card game Blackjack. It allows a player to play against a computerized dealer (the "krupier") by placing bets and making decisions to hit or stand based on their hand's current value. The game continues until the player chooses to stop or busts, at which point the krupier plays its hand. The winner is determined based on the comparison of hand values, and the player's chip count is adjusted accordingly. The game supports features such as shuffling, dealing, hitting, and standing, providing an interactive and enjoyable gaming experience.

### Future plans

- [ ] Enhance the user experience by developing a graphical user interface (GUI) using libraries like Tkinter or Pygame.
- [ ] Incorporate graphics and animations for cards, buttons, and other elements to make the game visually appealing.
- [ ] Add options to customize game settings such as the number of decks used, betting limits, and difficulty levels.
- [ ] Include sound effects for card shuffling, dealing, and button clicks. Background music can also enhance the gaming atmosphere.
- [ ] Keep track of game statistics such as win/loss ratio, total games played, and average bet size.
- [ ] Implement a multiplayer mode where players can compete against each other online or locally.
- [ ] Improve the intelligence of the computer-controlled krupier to make more strategic decisions based on the game state.
- [ ] Provide a tutorial or help section to explain the rules of the game and how to play.
- [ ] Allow players to save their progress and continue playing later. Implement a feature to load saved games.

## Bugdet tracker

Simple budget tracker that allows users to record their incomes, expenses, and recurring costs. It consists of several classes:

- Transaction: An abstract base class representing a generic financial transaction with attributes such as amount, description, and date.
- Income, Expense: subclasses of Transaction representing income and expense transactions.
- RecurringCost: A subclass of Transaction representing recurring expenses. It extends the Transaction class by adding attributes for start date, end date, and frequency of recurrence.
- BudgetTracker: A class that manages the tracking of incomes, expenses, and recurring costs. It provides methods to add transactions and calculate the net cash flow within a specified time period and display all transactions recorded.

### Future plans

- [ ] Implement error handling mechanisms to handle cases such as invalid input data, date inconsistencies, or overlapping recurring costs.
- [ ] Integrate a database or file system storage to persist transaction data between program executions.
- [ ] Provide more comprehensive reporting capabilities, such as generating monthly or yearly summaries, graphical representations of cash flow trends, or breakdowns by category.
- [ ] Develop a user-friendly interface, either through a graphical user interface (GUI) or a web application, to make it easier for users to interact with the budget tracker.
- [ ] Implement security measures to protect sensitive financial data, such as encryption of stored data and user authentication mechanisms.
- [ ] Implement notifications or alerts to notify users of upcoming bills, irregular spending patterns, or other important financial events.

## Calculator

Simple calculator implementation that utilizes a functional programming approach. The calculator function takes an initial argument and returns a nested function arg_collector. This nested function collects subsequent arguments and operators until it encounters the '=' operator, at which point it performs the arithmetic operations and returns the result. The test_calculator function contains test cases for addition, subtraction, multiplication, division, and exponentiation, verifying the correctness of the calculator implementation.

## Captcha maker

Project involves generating CAPTCHA images using various methods:

ImageCaptcha Generation: Utilizes the captcha.image library to generate a CAPTCHA image with random alphanumeric characters. The image is saved with the CAPTCHA text appended to the filename.

PIL (Python Imaging Library) Generation: Creates a CAPTCHA image using the PIL library. Similar to the first method, it generates random alphanumeric characters and draws them onto the image. The image is saved with the CAPTCHA text appended to the filename.

Captcha Solver Generation: This method utilizes a captcha solving library (captcha_solver) to generate CAPTCHA images. It generates random alphanumeric characters, saves the image, and returns the CAPTCHA text along with the path to the saved image.

### Future plans
- [ ] Allow customization of CAPTCHA parameters such as length, character set, image size, and font style.
- [ ] Evaluate the security implications of CAPTCHA generation, especially if the CAPTCHAs are intended for use in authentication or security-sensitive applications.
- [ ] If the project is intended for use by end-users, consider developing a simple command-line interface or web interface to make it more user-friendly.
- [ ] If the project is part of a larger application or framework, consider integrating it as a module or plugin to provide CAPTCHA functionality seamlessly.

## Company manager

Project models an employee management system for a company, providing classes to represent different types of employees and the company itself. Here's a breakdown of its components:
- Abstract Employee Class (Employee): An abstract base class defining the common interface for all types of employees. It includes an abstract method calculate_pay() to calculate the employee's pay.
- HourlyEmployee: Represents an employee paid based on hourly rate and hours worked.
- SalariedEmployee: Represents an employee with a fixed salary.
- Manager: Subclass of SalariedEmployee, representing a manager with an additional bonus component.
- Executive: Subclass of Manager, representing an executive with additional stock options.
- Company Class: Manages the hiring, firing, and raising of employees. It maintains a list of employees and provides methods to perform these actions.

## Complex number calculator

Perform basic arithmetic operations and other operations on complex numbers:
- add(a, b): Function to add two complex numbers a and b.
- sub(a, b): Function to subtract complex number b from complex number a.
- multi(a, b): Function to multiply two complex numbers a and b.
- negate(a): Function to negate (find the additive inverse) of a complex number a.
- invert(a): Function to find the multiplicative inverse of a complex number a.
- div(a, b): Function to divide complex number a by complex number b.
- conjugate(a): Function to find the conjugate of a complex number a.

### Future plans

- [ ] Implement error handling to handle cases where invalid input is provided, such as division by zero or non-numeric input.
- [ ] Implement special methods for arithmetic operators (__add__, __sub__, __mul__, __truediv__) in the Complex_number class. This will allow you to perform arithmetic operations using standard arithmetic operators (+, -, *, /).
- [ ] Implement additional operations commonly used with complex numbers, such as calculating the magnitude, phase angle, or converting between rectangular and polar form.
- [ ] Add type annotations to function parameters and return values to improve code readability and maintainability, especially if the project is part of a larger codebase.

## Distribution function

Project involves computing and comparing the values of the error function (Erf) and its approximations using different methods.

The project imports functions for exponential calculation (exp) and adaptive quadrature integration (KAdapt53) from external modules.

Functions:
- f(x): Defines a function representing the exponential function.
- S(a, b): Computes the integral of the exponential function between two points using adaptive quadrature integration.
- I(k): Computes the integral using S function for a given integer k.
- dystrybuanta(x): Computes the cumulative distribution function (CDF) of the standard normal distribution.
- fmt(num, dl): Formats a number into a string with a specified number of decimal places.

Main Calculation and Output: It calculates the values of the CDF for various input values of x and prints them along with the difference between the calculated values and the values obtained from math.erf and scipy.special.erf functions. 

Overall, the project focuses on computing and comparing the values of the error function and its approximations, providing insights into the accuracy of different computational methods for this task.

### Funkcja Exp

Function used in main program, for calculating the exponential function (Kexp) and its approximation (atnexp) using a series expansion. 

atnexp Function: Computes an approximation of the exponential function using a series expansion. It takes a single argument x and returns the approximate value of exp(x). The series expansion coefficients are stored in the atn list.

Computes the exponential function using a combination of rounding and series expansion. It rounds the input x and computes the exponential function using the atnexp function. The function also accounts for different powers of e based on the rounded value of x.

### Adapt53
Recursive function KAdapt53 for adaptive quadrature integration using Simpson's rule.

Inputs:
- a, c, b: Lower, midpoint, and upper bounds of the integration interval.
- fa, fc, fb: Function values at a, c, and b.
- func: The function to be integrated.
- eps: The desired tolerance for the error in the integration.

The function computes two approximations of the integral using Simpson's rule: one with a single step of third order (s3) and one with two steps of third order (s5). It then compares the absolute difference between these two approximations (s3 and s5) with the tolerance eps. If the difference is within tolerance, it returns the result computed with five steps of third order (Integ). If the difference is not within tolerance, the function recursively calls itself for the intervals [a, ac] and [c, b], where ac is the midpoint of [a, c] and cb is the midpoint of [c, b]. It then adds the results of these recursive calls and returns the total result. 

Output: The function returns the approximate value of the integral of func over the interval [a, b] with an error tolerance of eps.

## Doctor scheduler

Create a simple appointment scheduling system for doctors and patients.
- Patient Class: Represents a patient with attributes name and appointment_time.
- Doctor Class: Represents a doctor with attributes name, patients (list of patients), and work_time (defaulted to work hours from 8 AM to 4 PM). It has a method add_patient to schedule a patient's appointment with the doctor.
- Scheduler Class: Manages the scheduling of patients with doctors. It maintains a list of doctors and has a method schedule_patient to assign a patient to an available doctor.

### Future plans

- [ ] Allow doctors to specify their available appointment slots rather than a fixed number (e.g., 16) per day.
- [ ] Implement logic to handle cases where appointments overlap or exceed the doctor's work hours.
- [ ] Add error handling to deal with invalid input for appointment times or doctor's work hours.
- [ ] Implement a prioritization system for scheduling patients based on urgency or severity of their condition.
- [ ] Consider storing appointment data in a database or file for persistence across program executions.
- [ ] Develop a user interface (CLI, web, etc.) to interact with the scheduling system more intuitively.

## Event scheduler

## Family tree maker

## Flower shop

## GIF creator

## Graphs

## Interpolation

## Inverted index

## Limit calculator

## Mail checker

## Mortgage calculator

## Page scraper

## Pi number generator

## Pomodoro timer

## Product inventory

## Regex tool

## RSS Feed

## Site checker

## Tasks with numbers

## Tasks with strings

## Tax calculator

## Text editor

## Tik tak tok game

## Turtlu graphics

## Unit converter

## War card game

## Whois search
