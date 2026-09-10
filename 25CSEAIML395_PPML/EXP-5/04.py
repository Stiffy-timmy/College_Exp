s = set()

n = int(input("Enter number of elements: "))

for i in range(n):
    element = input("Enter element: ")
    s.add(element)

# Copy elements one by one
new_set = set()

for element in s:
    new_set.add(element)

print("Original set:", s)
print("New set:", new_set)
