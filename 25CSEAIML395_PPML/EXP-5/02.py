d = {'a': 10, 'b': 20, 'c': 20, 'd': 30, 'e': 40}

# Find unique values
unique_values = [value for value in d.values() if list(d.values()).count(value) == 1]

# Find maximum unique value
max_value = max(unique_values)

# Find and print its key
for key, value in d.items():
    if value == max_value:
        print("Key with maximum unique value:", key)
