# Enter first set
set1 = set()

n = int(input("Enter number of elements in first set: "))

for i in range(n):
    element = input("Enter string element: ")
    set1.add(element)

# Enter second set
set2 = set()

n = int(input("Enter number of elements in second set: "))

for i in range(n):
    element = input("Enter string element: ")
    set2.add(element)

# Combine both sets and remove duplicates
new_set = set1 | set2

print("First set:", set1)
print("Second set:", set2)
print("Combined set without duplicates:", new_set)
