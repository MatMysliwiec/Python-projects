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

Event Scheduler application built using the Tkinter library. It allows users to input event details such as date, time, and notes, and then add these events to a list. Key features include:

- Adding Events: Users can input the date (in YYYY-MM-DD format), time (in HH:MM format), and notes for the event. Invalid date or time formats are handled with error messages.
- Viewing Calendar: Users can view a list of all added events in a separate window. If no events are added, it notifies the user accordingly.
- Searching Events: Users can search for specific events by entering keywords. It displays matching events in a separate window. If no matching events are found, it notifies the user.

The application utilizes classes to manage events and the Tkinter library for creating a graphical user interface (GUI).

### Future plans

- [ ] Implement functionality to save and load events from a file.
- [ ] Provide more informative feedback to the user. Instead of just showing generic message boxes for success or failure, you can give more context-specific messages or use logging to keep track of events.
- [ ] Improve the user interface for better usability and aesthetics. You can add features like date picker widgets, tooltips for input fields, or use a different layout to make it more intuitive.
- [ ] Allow users to edit or delete events after they've been added. This could involve implementing context menus or buttons within the event list.
- [ ] Implement functionality to sort events by date or time, or allow users to filter events based on specific criteria like keywords or date ranges.
## Family tree maker

Python project defines classes for modeling a family tree and displaying it in a hierarchical structure.
- The Person class represents an individual with attributes such as name, birth year, death year (optional), and a list of children.
- The FamilyTree class takes a root person as input and constructs a family tree starting from that person.
- The display_tree method in the FamilyTree class recursively prints the family tree starting from a given person, including their children, grandchildren, and so on, with appropriate indentation to represent generations.

### Future plans

- [ ] Allow for more detailed information about individuals, such as gender, spouse(s), occupation, or any other relevant data.
- [ ] Implement methods to represent and manage various types of relationships, including marriages, divorces, adoptions, and step-parents.
- [ ] Implement different traversal methods for the family tree, such as depth-first search or breadth-first search, to perform various operations like finding ancestors or descendants.
- [ ] Add functionality to serialize/deserialize the family tree to/from a file, allowing for saving and loading family tree data for future use.
- [ ] Create a graphical user interface (GUI) to visualize the family tree graphically, making it more intuitive and interactive for users to explore and navigate.
- [ ] Implement methods to search and query the family tree, such as finding individuals by name, birth/death year, or other attributes, and retrieving relevant information about them.

## Flower shop


Python project models a simple flower shop system consisting of two main classes: Flower and Bouquet.

The Flower class represents individual flowers with attributes such as name, color, price per stem, and stock quantity. It includes methods to display information about the flower and to order more stems.

The Bouquet class represents a collection of flowers. It allows adding flowers to the bouquet, displaying the bouquet's composition, and calculating the total price of the bouquet based on the flowers' prices.

## GIF creator

Python script provides functions to convert images or videos to GIF format using the PIL library for images and the moviepy library for videos.

The create_from_image function takes an input folder containing image files, reads each image, and saves them as frames of a GIF. It allows specifying the output GIF path and the duration of each frame.

The convert_video_to_gif function converts a video file to a GIF. It reads the input video file, extracts each frame, and saves them as frames of a GIF. The duration parameter controls the frame rate of the resulting GIF.

To use the script, you need to specify the paths for the input images or video and the desired output GIF file. You can uncomment the create_from_image function call if you want to convert images instead of a video.


### Future plans

- [ ] Add input validation to ensure that the provided input paths are valid and that the files exist before attempting to convert them. You can also check if the input images or video have the correct format and dimensions for conversion.
- [ ] Enhance user interaction by providing command-line arguments or a graphical user interface (GUI) to specify input and output paths, as well as additional options like frame duration or output resolution.

## Graphs

### Eulerian path
Code utilizes the NetworkX library to determine whether a given graph has an Eulerian path, Eulerian cycle, or neither, and provides a visualization of the graph if applicable.

The find_eulerian_path_or_cycle function takes a graph as input and checks if it's connected. If the graph is connected, it then identifies nodes with odd degrees. Based on the number of nodes with odd degrees, it determines whether the graph has an Eulerian path, Eulerian cycle, or neither.

The visualize_graph function visualizes the input graph using matplotlib. It positions the nodes using the spring layout algorithm and draws the graph with labels.

An example graph is created using the NetworkX library, and edges are added to it. The find_eulerian_path_or_cycle function is called to determine if the graph has an Eulerian path or cycle, and the result is printed.

### Graph from links
Code utilizes the NetworkX library to create, analyze, and visualize a graph. It includes functions to create a graph, check if it's connected, and draw it using different layout algorithms.

The create_graph function takes a list of links (edges) as input and constructs an undirected graph using NetworkX. It then adds the edges from the input list to the graph.

The is_connected function determines whether the input graph is connected using the is_connected function from NetworkX. It prints a message indicating whether the graph is connected or not.

The draw_graph function visualizes the input graph using matplotlib. It positions the nodes using a specified layout algorithm (in this case, circular layout), and then draws the graph with labels.

Different layout algorithms are provided as comments within the draw_graph function, allowing users to experiment with different layouts for graph visualization.

### Minimum spanning tree

Code implements the Kruskal's algorithm for finding the minimum spanning tree (MST) of a given weighted graph using NetworkX.

The kruskal function takes a graph represented as a dictionary where the keys are nodes and the values are lists of tuples containing neighboring nodes and edge weights. It constructs a NetworkX graph G from this input. It then uses the nx.minimum_spanning_tree function to find the minimum spanning tree of the graph G. This function returns a minimum spanning tree as a NetworkX graph. Finally, it extracts the edges of the minimum spanning tree along with their weights and returns them as a list of tuples containing (source, target, weight).

## Image gallery (still working on it)
Python code defines an Image Gallery application using Tkinter for the graphical user interface (GUI) and OpenCV for image processing.

The ImageBase abstract base class defines two abstract methods: load for loading an image from a file, and display for displaying the image on a canvas.

The JPEGImage class implements the ImageBase interface for handling JPEG images. It loads JPEG images using OpenCV (cv2) and resizes them for display on the canvas.

The ImageGalleryApp class represents the main application. It loads a list of image paths, creates instances of JPEGImage for each image, and displays them in a grid layout using Tkinter's Canvas widget.

## Interpolation

Python code performs Lagrange interpolation on a set of data points and visualizes the results using matplotlib.

It imports two functions KSin and Pipol from the module Interpolacja.FunkcjaSin and the interpol function from the Interpolacja module. The Kread function reads data from a file and extracts x and y values from each line. The main part of the code defines the data points, calculates interpolated values at a specific point x0, and compares them with the exact values obtained from KSin.
It then generates additional points for plotting the exact curve (x_rz, y_rz) and the interpolated curve (x_int, y_int) using the calculated interpolated values.
Finally, it visualizes the original data points, exact curve, and interpolated curve using scatter plots with matplotlib.

This code demonstrates the usage of Lagrange interpolation to approximate a function from a set of data points and visualizes the results for comparison.

## Inverted index

Python code builds an inverted index from text files in a specified directory and allows users to search for terms within those files using the inverted index.

The build function takes a list of file paths as input, reads each file, tokenizes its content into words, and constructs an inverted index where each word maps to a list of files containing that word.

The search function takes the inverted index and a search query as input, tokenizes the query into words, and retrieves files containing any of the query words from the inverted index.

In the main block, the directory containing the text files is specified, and the files in that directory are collected. The inverted index is built from these files. A while loop allows users to input search queries. The loop continues until the user inputs "exit". For each search query, the search function is called, and the matching files are printed.

## Limit calculator

Python script calculates the limit of a given function as x approaches a specified value. It uses the sympy library to perform symbolic calculations.

The limit_calculator function prompts the user to input a function in terms of x and the value of the limit. It then evaluates the limit of the function using sympy's limit function.
If the user inputs 'oo' (infinity) as the limit value, the script assigns the sympy symbol oo to represent infinity.
The result of the limit calculation is then printed to the console.

### Future plans

- [ ] Implement input validation to handle invalid user inputs, such as non-numeric limit values or invalid function syntax.
- [ ] Add error handling to catch exceptions that may occur during function evaluation or limit calculation, providing informative error messages to the user.
- [ ] Extend the script to support more complex functions, including trigonometric, exponential, and logarithmic functions, by importing them from sympy and allowing users to input them.

## Mail checker

Python script checks for unread emails using the IMAP protocol, allowing users to monitor their inbox periodically.

The check_email_imap function connects to the specified email server using IMAP4_SSL, logs in with the provided credentials, and selects the "inbox" folder. It then searches for unread messages using the IMAP SEARCH command and retrieves their IDs.
If there are unread emails, it fetches their details, such as the date and subject, and prints them to the console. The script then enters a loop where it repeatedly calls check_email_imap at the specified interval. It continues checking for emails until the user interrupts the program with Ctrl+C.

### Future plans

- [ ] Enhance error handling to gracefully handle exceptions, providing meaningful error messages and handling different types of errors appropriately.
- [ ] Improve security by encrypting the user's password input or using more secure authentication methods, such as OAuth, instead of directly entering passwords.
- [ ] Add logging functionality to record important events and errors, making it easier to debug issues and monitor the script's behavior over time.
- [ ] Implement optimizations to reduce unnecessary network requests or resource consumption, such as caching email IDs or using IDLE mode for real-time updates from the server.
- [ ] Building a graphical user interface (GUI) for the email checker to provide a more user-friendly experience, especially for less tech-savvy users.

## Mortgage calculator

Code calculates the monthly payment and total repayment for a mortgage loan based on the loan amount, annual interest rate, loan terms in years, and compounding interval in Poland.

### Future plans
- [ ] Implement input validation to ensure that the user inputs are valid numeric values and that the compounding interval is one of the accepted options.
- [ ] Consider splitting the calculation logic into separate functions to improve readability and maintainability, especially for complex calculations.

## MP3 player (working on it)

Python script creates a simple MP3 player GUI using Tkinter and pygame libraries. Users can add MP3 files to a playlist, play, pause, stop, and navigate through tracks.

## Mp3 tagger

Python script utilizes the eyed3 library to modify ID3 tags of audio files, such as MP3 files. It allows users to update various metadata attributes of the audio file, including title, artist, album, year, track number, genre, album art, and additional custom tags.
    
## Networking

### Country IP
Python script utilizes the requests library to retrieve information about a given IP address or the public IP address of the user. It interacts with the IPinfo.io API to obtain data such as the country associated with the IP address.

### Port scanner

Python script performs port scanning on a target IP address within a specified range of ports. It utilizes the socket module to establish TCP connections to each port and determines whether the port is open or closed.

## Online whiteboard (working on it)
Implements a simple networked whiteboard using curses and sockets. Users can connect to the whiteboard server and draw on it, and their drawings are displayed to all connected clients.

## Page scraper

Python script defines a PageScraper class that extracts links and image URLs from a specified webpage using the requests and BeautifulSoup libraries. It then saves the extracted links and image URLs to separate text files.

### Future plans

- [ ] Implement error handling to handle cases where the request to the webpage fails or parsing of the HTML content encounters errors. This ensures the script gracefully handles unexpected situations.
- [ ] Enhance URL handling to support relative URLs and normalize extracted URLs to ensure they are valid and consistent.
- [ ] Implement rate limiting or throttling mechanisms to prevent overwhelming the target server with too many requests in a short period, which can lead to IP blocking or server overload.
- [ ] Introduce logging to capture diagnostic information, such as request/response details, errors, and progress updates, for debugging and monitoring purposes.
    
## PDF generator (working on it)

Flask application (app.py) serves a webpage with a form allowing users to upload HTML content. Upon submitting the form, the server generates a PDF file from the uploaded HTML content using WeasyPrint and sends the generated PDF file back to the user as an attachment.

## Pi number generator

Python script calculates the value of pi using the Gauss-Legendre algorithm and allows the user to specify the number of digits for the output. Here's a breakdown of the script:

## Pomodoro timer

Python script implements a Pomodoro Timer application using Tkinter.

PomodoroTimer Class:
        It represents the main application window.
        Initializes the GUI elements such as labels and buttons for the timer and settings.
        Provides methods for managing the timer, updating the timer display, toggling the timer, and resetting the timer.
        Allows users to set work duration, break duration, and the number of cycles through a settings dialog.

show_settings_dialog Method:
        Displays a settings dialog for users to set work duration, break duration, and the number of cycles.
        Updates the total time based on the settings provided.

apply_settings Method:
        Applies the settings chosen by the user.
        Validates the input values before applying the settings.
        Starts the timer after applying the settings.

start_pomodoro_timer Method:
        Starts the Pomodoro timer with the specified work duration, break duration, and number of cycles.

toggle_timer Method:
        Toggles the timer between pause and resume states.

update_timer Method:
        Updates the timer display and manages the timer logic (work duration, break duration, cycles).
        Plays an alarm when the timer finishes a work or break period.

reset_timer Method:
        Resets the timer to its initial state.
        Cancels any ongoing timer updates.

display_time Method:
        Formats and displays the remaining time in minutes and seconds.

display_info Method:
        Displays information about whether it's work time or break time and the current cycle number.

### Future plans

- [ ] Enhance the user interface with additional features, styles, or themes to improve usability and aesthetics.
- [ ] Support multiple languages or locales to make the application more accessible to a broader audience.
- [ ] Making the app which can connect to the computer and display timer in owner phone

## Product inventory

Python code defines two classes: Product and Inventory, which together simulate a simple inventory management system.

Product Class:
initializes a product with attributes such as product_id, name, price, and quantity, returns a string representation of the product, calculates and returns the total value of the product based on its price and quantity.

Inventory Class:
method adds a new product to the inventory, iterates through the products in the inventory, calculates the total value of all products, and returns it, prints out details of each product in the inventory.

## Regex tool

Code defines a simple GUI application using Tkinter for running regular expression queries on text.

### Future plans

- [ ] Implement input validation to handle cases where the text or regular expression pattern is empty.
- [ ] Add a button to clear the text and result fields for better usability.
- [ ] Add a vertical scrollbar to the result text widget to handle cases where there are many matches.
- [ ] Optionally, display the matched substrings in addition to their indices for better context.

## RSS Feed

Code retrieves and displays data from an RSS feed using the feedparser library.

### Future plans

- [ ] Implement more specific error handling to handle different types of exceptions that may occur during feed parsing and display.
- [ ] Optionally, extract and display additional information from the feed entries, such as author, category, or content.
- [ ] Utilize Python's logging module to log errors and other relevant information instead of printing directly to the console.
- [ ] Validate the input feed URL to ensure it is a valid URL before attempting to parse it.

## Site checker

Script checks the status of a website at regular intervals using the requests library and sends an email notification if the website is down.

check_website Function:
        Takes a URL as input.
        Sends an HTTP GET request to the URL using requests.get.
        Checks if the response status code is 200 (OK).
        Prints a message indicating whether the website is up or down.
        If the website is down, calls the send_email function to send an email notification.
        Returns True if the website is up and False if it's down.

send_email Function:
        Takes the URL of the down website as input.
        Configures the email sender, recipient, subject, and body.
        Sends an email using the SMTP server of the sender's email provider (in this case, Gmail).

job Function:
        Defines a job that checks the website status and prints a message with the current timestamp.
        Calls the check_website function to perform the website status check.


### Future plans

- [ ] Use environment variables or a configuration file to store sensitive information such as email credentials rather than hardcoding them in the script.
- [ ] Implement more robust error handling to catch and handle exceptions that may occur during email sending or scheduling.
- [ ] Make the email sender, recipient, and SMTP server configurable via command-line arguments or a configuration file.
- [ ] Add a mechanism to gracefully handle script termination, such as catching KeyboardInterrupt and performing cleanup tasks.
- [ ] Implement a retry mechanism in case of transient errors, such as connection errors or timeouts, during website checking or email sending.

## Slide show (working on it)

Code is a simple slideshow application built using Tkinter in Python. It displays a sequence of images with a fade-out transition effect between each image.

## Sort Excel(working on it)

Code sorts a CSV file based on a specified column and sort order using the pandas library. 

## Stream video

Code defines two functions download_video and play_video:

download_video: This function takes a YouTube video URL as input and downloads the video in MP4 format with progressive streaming. It uses the pytube library to fetch the YouTube video and download it to the specified output path (or "video.mp4" by default).

play_video: This function takes the path to a video file as input and plays the video using OpenCV's cv2 module. It opens the video file using cv2.VideoCapture and reads each frame of the video. It then displays each frame in a window named "Online Video Player" until the video ends or the user presses the 'q' key.

## Tasks with numbers
### Numerical integration methods using Simpson's 3/8 rule

Code you provided seems to be implementing numerical integration methods using Simpson's 3/8 rule (s3) and Simpson's 5/8 rule (s5). These methods are used to approximate definite integrals numerically.

### Change return

Python function calculates the change to be returned to a customer given the cost of an item and the amount of money provided by the customer. It then prints the breakdown of the change in terms of quarters, dimes, nickels, and pennies.

### Coin flip simulation
Python code simulates flipping a coin a specified number of times and records the outcomes (heads or tails). 

### Cost of Tile

Python function calculates the total cost of tiles needed to cover a floor given the dimensions of the floor (width and height) and the price of the tile per square meter.
### Credit card validation

Function valid_credit_card checks whether a given credit card number is valid according to the Luhn algorithm. Here's a breakdown of how it works:

The function takes a number parameter, which represents the credit card number.

The credit card number is first sanitized by removing any spaces.

If the length of the sanitized number is not 16 (the standard length for credit card numbers), the function immediately returns False.

The function then initializes three sums (sum1, sum2, and sum3) to calculate the checksum according to the Luhn algorithm.

It iterates over the digits of the credit card number, doubling every other digit starting from the second-to-last digit (index 15) and summing the results in sum1.

It sums the digits that were not doubled in sum2.

It counts the number of digits greater than 4 in the doubled digits and adds this count to sum3.

The checksum is calculated as the sum of sum1, sum2, and sum3.

The check digit is computed as 10 - (checksum % 10).

If the check digit matches the last digit of the credit card number (index 15), the function returns True, indicating that the credit card number is valid. Otherwise, it returns False.

### Distance city

This script utilizes the geopy library to calculate the distance between two cities using their coordinates obtained via the Nominatim geocoding service. 

### Factorial finder

This script calculates the factorial of a positive integer entered by the user using both a loop and recursion. 

### Fibonacci

Generates the Fibonacci sequence up to the nth term using a recursive approach

### Happy numbers

A happy number is defined by the following process. Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.

### Number names

Script takes a number as input and converts it into words, following the English naming convention.

### Prime factorization

Script finds the prime factors of a given number using trial division.

### Prime generator

Script generates prime numbers continuously until the user decides to exit. 

### Shape perimeter

Code defines a simple hierarchy of geometric shapes using Python's abstract base class module (abc). this code provides a simple framework for representing and working with geometric shapes in Python. It demonstrates the concept of inheritance and polymorphism, allowing different shapes to be treated uniformly through a common interface (Shape).

## Tasks with strings
### Atomic clock

Code fetches the current atomic time from an NTP (Network Time Protocol) server using the ntplib library.

### Count Vowels

Code defines a function count_vowels(word) that counts the number of vowels in a given word. 

### Count words

Function takes a string as input and counts the number of words in the string

### Encrypt and decrypt

Code defines two encryption algorithms: Vigenère cipher and Caesar cipher, along with their corresponding decryption functions.

### Fizz Buzz
Code implements the FizzBuzz problem, which is a classic programming exercise. Here's a brief overview of how it works:

It creates a list of numbers from 1 to 100 using a list comprehension.
    It iterates over each number in the list and checks if the number is divisible by 3, 5, or both.
    If the number is divisible by both 3 and 5, it replaces the number with "FizzBuzz".
    If the number is divisible by 3 only, it replaces the number with "Fizz".
    If the number is divisible by 5 only, it replaces the number with "Buzz".
    Finally, it prints the updated list.
### Pig latin
Function takes a word as input and converts it into Pig Latin based on the following rules:

If the word begins with a vowel, "way" is added to the end of the word.

If the word begins with a consonant, all consonants before the first vowel are moved to the end of the word, and "ay" is added.

## Tax calculator

Code snippet appears to be a simple tax calculator that calculates the Personal Income Tax (PIT) based on the given income and deductible costs.

## Text editor

This code implements a basic text editor GUI using Tkinter in Python. It allows users to open, save, and save files with a graphical interface.

### Future plans
- [ ] Implement error handling for file operations such as opening and saving files. This will make the application more robust and user-friendly.
- [ ] Add confirmation dialogs for actions like exiting the application or overwriting existing files when saving. This helps prevent accidental data loss.
- [ ] Consider organizing the menu items logically.
- [ ] Provide keyboard shortcuts for common actions like opening and saving files.
- [ ] Add a status bar to display information such as the current file name, word count, or cursor position. This gives users feedback on their actions and enhances the overall user experience.
- [ ] Allow users to customize the appearance of the text editor by providing theme options such as font size, font type, and color schemes.
- [ ] Implement additional text editing features such as copy, cut, paste, undo, redo, and find/replace. These features improve the utility of the text editor for users.


## Tik tak tok game
Code implements a simple Tic Tac Toe game using Python's console interface. Players can input their names and choose their markers ('X' or 'O') to start the game. The game continues until one player wins or there is a draw. Players can also choose to play again once the game is over.

### Future plans

- [ ] Implement error handling for user inputs to handle unexpected inputs gracefully. For example, you can handle cases where players enter non-numeric values or choose positions that are already occupied.
- [ ] Instead of printing new game boards below the previous ones, clear the console screen before displaying each new board. This provides a cleaner user interface.
- [ ] Consider building a graphical user interface (GUI) using libraries like Tkinter or PyQt to enhance the user experience. A GUI can provide visual feedback, better controls, and a more engaging interface for the players.

## Unit converter
Code is a simple unit converter GUI built using Tkinter. Users can select the type of conversion (temperature, length, area, volume, or weight) and input the value they want to convert from and to. The conversion results are displayed in the corresponding entry field.

### Future plans

- [ ] Consolidate this code by creating a single conversion function that takes parameters for the conversion factors and units.
- [ ] Implement input validation to handle invalid inputs gracefully. For example, check if the user input is a valid number before performing the conversion. You've started doing this in some places, but it can be extended to cover all user inputs.
- [ ] Add error handling to catch exceptions that may occur during conversion (e.g., division by zero). Display meaningful error messages to the user if something goes wrong.
- [ ] Consider enhancing the user interface by adding labels to indicate what each input field represents and improving the layout for better readability.

## War card game
Code implements the card game "War" where two players compete against each other by playing cards from their decks. 

### Future plans
- [ ] Variable names like kolory, numery, and wartosci are in Polish, change to English.
- [ ] Consider adding error handling for scenarios like incorrect user input or unexpected behavior during the game.
- [ ] The game logic seems correct, but you might want to consider edge cases and corner scenarios to ensure the game behaves as expected in all situations.
- [ ] Consider adding features like a graphical user interface, multiplayer support over a network, or different game modes to make the game more interesting.

## Watermarking (working on it)
Code adds a watermark to images concurrently using threading.

## Whois search
Code performs a WHOIS lookup using the IPWhois library.

### Future plans

- [ ] Ensure that the user input is validated before performing the WHOIS lookup. This is important to prevent malformed or malicious input from causing unexpected behavior or security issues.
- [ ] Currently prints the WHOIS results directly to the console. Depending on your application, you might want to return the results from the whois_lookup function instead, allowing the caller to decide how to handle the output (e.g., display it in a GUI, save it to a file, etc.).

## Zip File creator (working on it)
Script allows users to compress multiple files into a single ZIP archive. 
