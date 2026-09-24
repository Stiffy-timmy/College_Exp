# WAP to convert a given list of intefers and a tuple of intefers in a list of string using map()
def to_string(data):
    return list(map(str, data))

print(to_string([1, 2, 3]))
print(to_string((4, 5, 6)))