# Create an empty list
lst = []

# Input number of elements
n = int(input("Enter number of elements: "))

# Input elements into the list
for _ in range(n):
    lst.append(int(input()))

# Remove duplicates and sort the list
lst = sorted(set(lst))

# Print the final list
print("Sorted list without duplicates:", lst)
