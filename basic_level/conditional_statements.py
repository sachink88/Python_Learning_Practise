# conditional_statements.py
# This script demonstrates the use of conditional statements: if, elif, and else with user input and multiple examples.

# 1. Simple if statement
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")

# 2. if-else statement
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# 3. if-elif-else: Check number type
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 4. Nested conditions: Check age category
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 5. String condition example
name = input("Enter your name: ")
if name == "Sachin":
    print("Hello Sachin, nice to see you!")
else:
    print(f"Hello {name}!")

# 6. Multiple conditions using 'and'/'or'
score = int(input("Enter your test score (0-100): "))
if score >= 90 and score <= 100:
    print("Excellent!")
elif score >= 75:
    print("Good job!")
elif score >= 50:
    print("Needs improvement.")
else:
    print("Try harder next time.")

# End of conditional_statements.py
