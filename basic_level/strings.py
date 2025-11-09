# strings.py
# This script explains how to use and manipulate strings in Python, with practical examples.

# 1. Creating and printing strings
greeting = "Welcome to Python string handling!"
print(greeting)

# 2. String concatenation (joining)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Your full name is:", full_name)

# 3. String length
print("Length of your full name:", len(full_name))

# 4. Accessing characters by index
print("First letter of your first name:", first_name[0])
print("Last letter of your last name:", last_name[-1])

# 5. Slicing strings (get part of the string)
print("First three letters of your first name:", first_name[:3])
print("Last two letters of your last name:", last_name[-2:])

# 6. Changing case
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())

# 7. Removing spaces (stripping)
sample_str = "   Python is fun!   "
print("Original:", repr(sample_str))
print("Without leading/trailing spaces:", sample_str.strip())

# 8. Finding and replacing text
sentence = "I love learning Python. Python is great!"
print("Position of 'Python':", sentence.find("Python"))   # First occurrence
print("Replace 'Python' with 'programming':", sentence.replace("Python", "programming"))

# 9. Splitting and joining strings
hobbies = input("Enter your hobbies (comma separated): ")      # e.g., reading,coding,gaming
hobby_list = hobbies.split(",")                                # Splits into list
print("Your hobbies as a list:", hobby_list)
joined_hobbies = " | ".join(hobby_list)                        # Joins list as a string
print("Your hobbies (joined):", joined_hobbies)

# End of strings.py
