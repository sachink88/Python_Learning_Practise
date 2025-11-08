# loops.py
# This script explains how to use loops in Python: for loop, while loop, break, and continue with practical examples.

# 1. for loop: Print numbers from 1 to 5
print("Numbers from 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

# 2. for loop: Print each character in a string
word = input("Enter a word: ")
print("Characters in the word using for loop:")
for ch in word:
    print(ch)

# 3. while loop: Print numbers from 1 to 5
print("Numbers from 1 to 5 using while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment by 1

# 4. break statement: Stop loop when a condition is met
print("Display numbers until 7 is reached (using break):")
for num in range(1, 11):
    if num == 7:
        print("Reached 7, stopping the loop.")
        break
    print(num)

# 5. continue statement: Skip a value in the loop
print("Print odd numbers from 1 to 10 (using continue):")
for num in range(1, 11):
    if num % 2 == 0:
        continue   # Skip even numbers
    print(num)

# 6. Using loops with user input: Sum of numbers
n = int(input("Enter how many numbers to sum: "))
total = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total += num
print(f"Total sum is: {total}")

# End of loops.py
