dict1 = {}
dict2 = {}

n1 = int(input("Enter number of inputs(dict-1): "))
for i in range(n1):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    dict1[key] = value

n2 = int(input("Enter number of inputs(dict-2): "))
for j in range(n2):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    dict1[key] = value

dict1.update(dict2)
print(f"Merged Dictionary is: {dict1}")
