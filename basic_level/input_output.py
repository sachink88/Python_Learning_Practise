# input_output.py
# This script covers basic input from the user and output to the console in Python.

# 1. Output: Using print() to display information
print("Welcome to Python!")  # Output: Welcome to Python!

# 2. Getting input from the user
# The input() function reads a line from the console as a string.
user_name = input("Enter your name: ")  # Prompts user to type their name
print("Hello,", user_name)              # Outputs: Hello, Sachin (if you typed Sachin)

# 3. Input is always taken as a string. If you need a number, convert it.
age = input("Enter your age: ")         # User enters age, e.g., 25
print("Type of age before conversion:", type(age))  # <class 'str'>

age = int(age)                         # Convert string input to integer
print("Type of age after conversion:", type(age))   # <class 'int'>
print("Next year, you will be", age + 1)

# 4. Taking multiple inputs in one line (split and unpack)
numbers = input("Enter two numbers separated by space: ")  # e.g., 5 10
num1, num2 = numbers.split()
num1 = int(num1)
num2 = int(num2)
print("Sum:", num1 + num2)

# 5. Getting a float number from user
height = float(input("Enter your height in meters: "))      # e.g., 1.76
print("Your height is", height, "meters.")

# 6. Formatting output
print(f"{user_name} is {age} years old and {height} meters tall.")

# End of input_output.py
