# functions.py
# This script explains how to define and use functions in Python, with several practical examples.

# 1. Defining a simple function
def greet():
    print("Hello from the greet() function!")

# 2. Calling the function
greet()

# 3. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

user_name = input("Enter your name: ")
greet_person(user_name)

# 4. Function with parameters and return value
def add_numbers(a, b):
    sum_result = a + b
    return sum_result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add_numbers(num1, num2)
print(f"The sum is: {result}")

# 5. Function with default parameter value
def welcome(message="Welcome to Python functions!"):
    print(message)

welcome()  # Uses default message
welcome("Custom welcome message!")  # Uses provided message

# 6. Function to find factorial of a number
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

number = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {number} is {factorial(number)}")

# End of functions.py
