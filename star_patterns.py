"""
star_patterns.py
Basic Python script to print common star patterns.

Author: Sachin Kabade
"""

# 1. Square pattern
def square_pattern(n):
    for i in range(n):
        print("* " * n)

# 2. Right triangle pattern
def right_triangle(n):
    for i in range(1, n+1):
        print("* " * i)

# 3. Inverted right triangle
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

# 4. Pyramid pattern
def pyramid_pattern(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

# Basic runner
if __name__ == "__main__":
    rows = 5  # Feel free to change for demo

    print("Square pattern:")
    square_pattern(rows)
    print("\nRight triangle pattern:")
    right_triangle(rows)
    print("\nInverted triangle pattern:")
    inverted_triangle(rows)
    print("\nPyramid pattern:")
    pyramid_pattern(rows)
