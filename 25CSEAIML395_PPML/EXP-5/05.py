# Enter first set
set1 = set()

n = int(input("Enter number of elements in first set: "))

for i in range(n):
    element = input("Enter element: ")
    set1.add(element)

# Enter second set
set2 = set()

n = int(input("Enter number of elements in second set: "))

for i in range(n):
    element = input("Enter element: ")
    set2.add(element)

# Display the sets
print("First set:", set1)
print("Second set:", set2)

# Set operations
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set1 - Set2):", set1 - set2)
print("Difference (Set2 - Set1):", set2 - set1)
print("Symmetric Difference:", set1 ^ set2)
