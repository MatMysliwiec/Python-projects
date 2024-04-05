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

### Future improvement
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

### Future improvement
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

## Calculator

## Captcha maker

## Company management

## Complex number calculator

## Distribution function

## Doctor scheduler

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
