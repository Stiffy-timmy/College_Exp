# WAP to add three given list using python map and lambda 
def add_lists(a, b, c):
    return list(map(lambda x, y, z: x + y + z, a, b, c))

print(add_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]))   