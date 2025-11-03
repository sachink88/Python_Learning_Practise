# variables_and_data_types.py
# This script explains how to use variables and the most common data types in Python.

# 1. Variables: Assigning values
name = "Sachin"       # string
age = 34              # integer
height = 1.76         # float (decimal number)
is_data_engineer = True   # boolean

print(name)           # Output: Sachin
print(age)            # Output: 34
print(height)         # Output: 1.76
print(is_data_engineer)   # Output: True

# 2. Type checking: Use 'type()' to check a variable's data type
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_data_engineer)) # <class 'bool'>

# 3. Multiple assignment
city, country = "Mumbai", "India"
print(city, country)  # Output: Mumbai India

# 4. Changing the value/type of a variable
score = 50           # integer
score = "Fifty"      # Now string
print(score)         # Output: Fifty

# 5. Type conversion (casting)
a = "123"            # string
b = int(a)           # convert to integer
c = float(a)         # convert to float
d = str(b)           # convert integer to string

print(b)             # Output: 123
print(c)             # Output: 123.0
print(d)             # Output: '123'

# 6. Basic operations
num1 = 10
num2 = 3
print(num1 + num2)   # Addition, Output: 13
print(num1 - num2)   # Subtraction, Output: 7
print(num1 * num2)   # Multiplication, Output: 30
print(num1 / num2)   # Division (float), Output: 3.333...
print(num1 // num2)  # Integer division, Output: 3
print(num1 % num2)   # Modulo, Output: 1

# 7. Constants: Python does not have true constants, but you can use ALL CAPS by convention
PI = 3.14159
print(PI)            # Output: 3.14159

# 8. Special values: None indicates no value
middle_name = None
print(middle_name)   # Output: None

# End of variables_and_data_types.py
