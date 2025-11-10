# list_operations.py
# This script covers all essential operations with lists: creating empty lists, indexing, slicing,
# adding, removing, sorting, copying, and more—with clear comments and examples.

# 1. Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# 2. Creating a list with values
numbers = [5, 2, 9, 1, 7]
print("Original numbers list:", numbers)

# 3. Indexing (access specific elements)
print("First element:", numbers[0])      # Output: 5
print("Last element:", numbers[-1])      # Output: 7

# 4. Slicing (get portions of the list)
print("First three numbers:", numbers[:3])    # Output: [5, 2, 9]
print("All except first:", numbers[1:])       # Output: [2, 9, 1, 7]
print("Middle part:", numbers[1:4])           # Output: [2, 9, 1]

# 5. Adding elements
numbers.append(10)                      # Add at end
print("After appending 10:", numbers)

numbers.insert(2, 20)                   # Insert at index 2
print("After inserting 20 at index 2:", numbers)

# 6. Removing elements
numbers.remove(9)                       # Remove first occurrence of 9
print("After removing 9:", numbers)

removed_item = numbers.pop()            # Remove last item
print("After popping last item:", numbers)
print("Popped item:", removed_item)

removed_at_index = numbers.pop(1)       # Remove item by index
print("After popping index 1:", numbers)
print("Popped item at index 1:", removed_at_index)

# 7. Updating list elements by index
numbers[0] = 100                        # Change first element
print("After updating first element to 100:", numbers)

# 8. Checking existence
if 7 in numbers:
    print("7 found in numbers list.")
else:
    print("7 not found in numbers list.")

# 9. Sorting and reversing a list
numbers.sort()                          # Sort ascending
print("Sorted list:", numbers)

numbers.reverse()                       # Reverse order
print("Reversed list:", numbers)

# 10. Copying a list
numbers_copy = numbers.copy()           # Shallow copy
print("Copied list:", numbers_copy)

# 11. List length
print("Length of numbers list:", len(numbers))

# 12. Clearing a list (remove all elements)
numbers.clear()
print("After clearing, numbers list:", numbers)

# End of list_operations.py
