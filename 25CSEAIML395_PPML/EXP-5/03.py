d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

new_dict = {}

for key, value in d.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Dictionary after removing duplicate values:", new_dict)
