# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]

# Access elements using indexing
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# Modify elements in the list
fruits[1] = "Kiwies"  # Change 'Banana' to 'Kiwies'
print(f"\nModified list is: {fruits}")

# Add an element to the list
fruits.append("Watermelon")
print(f"After adding Watermelon: {fruits}")

# Remove an element from the list
fruits.remove("Watermelon")
print(f"After removing Watermelon: {fruits}")

# Find the length of the list
length = len(fruits)
print(f"\nLength of the list: {length}")

# Sort the list in ascending order
fruits.sort()
print(f"\nSorted list in ascending order: {fruits}")

# Sort the list in descending order
fruits.sort(reverse=True)
print(f"Sorted list in descending order: {fruits}")