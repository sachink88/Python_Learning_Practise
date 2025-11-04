# burger_order.py
# This script demonstrates variables, input/output and a simple burger ordering logic.

# 1. Welcome message
print("Welcome to Burger Palace!")

# 2. Ask user for their name
customer_name = input("Please enter your name: ")
print(f"Hello, {customer_name}! Ready to place your order?")

# 3. Ask user how many burgers they want
burger_count = int(input("How many burgers would you like to purchase? "))

# 4. Ask the price per burger
price_per_burger = float(input("Enter price per burger (₹): "))

# 5. Calculate total cost
total_cost = burger_count * price_per_burger

# 6. Display the total cost
print(f"\nOrder Summary for {customer_name}:")
print(f"Burgers Ordered: {burger_count}")
print(f"Price per Burger: ₹{price_per_burger}")
print(f"Total Cost: ₹{total_cost}")

# 7. Ask user how many burgers they like to eat in a month (`variable + input`)
monthly_like = int(input("How many burgers do you LIKE to eat in a month? "))

# 8. Fun message based on input
if monthly_like >= 10:
    print("Wow! You're a burger lover 🍔!")
elif 5 <= monthly_like < 10:
    print("You enjoy burgers quite often.")
else:
    print("Burgers are an occasional treat for you.")

# End of burger_order.py
