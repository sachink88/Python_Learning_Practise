# operators.py
# This script explains the different types of operators in Python with user input and examples.

# 1. Arithmetic Operators
print("Arithmetic Operators Demo")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")    # Addition
print(f"{num1} - {num2} = {num1 - num2}")    # Subtraction
print(f"{num1} * {num2} = {num1 * num2}")    # Multiplication
print(f"{num1} / {num2} = {num1 / num2}")    # Division (float)
print(f"{num1} // {num2} = {num1 // num2}")  # Integer (floor) division
print(f"{num1} % {num2} = {num1 % num2}")    # Modulus (remainder)
print(f"{num1} ** {num2} = {num1 ** num2}")  # Exponentiation

print("\nComparison Operators Demo")
# 2. Comparison Operators
print(f"{num1} == {num2}: {num1 == num2}")   # Equality
print(f"{num1} != {num2}: {num1 != num2}")   # Not equal
print(f"{num1} > {num2}: {num1 > num2}")     # Greater than
print(f"{num1} < {num2}: {num1 < num2}")     # Less than
print(f"{num1} >= {num2}: {num1 >= num2}")   # Greater or equal
print(f"{num1} <= {num2}: {num1 <= num2}")   # Less or equal

print("\nLogical Operators Demo")
# 3. Logical Operators
result = (num1 > 0 and num2 > 0)
print(f"Are both numbers positive? {result}") # AND operator

result = (num1 > 0 or num2 > 0)
print(f"Is at least one number positive? {result}") # OR operator

result = not(num1 > num2)
print(f"Is num1 NOT greater than num2? {result}")   # NOT operator

print("\nAssignment Operators Demo")
# 4. Assignment Operators
value = num1      # Basic assignment
print(f"Initial value: {value}")
value += num2     # value = value + num2
print(f"After += : {value}")
value -= num2     # value = value - num2
print(f"After -= : {value}")
value *= 2        # value = value * 2
print(f"After *= : {value}")
value /= 2        # value = value / 2
print(f"After /= : {value}")

print("\nEnd of operators.py demo!")

# End of operators.py
