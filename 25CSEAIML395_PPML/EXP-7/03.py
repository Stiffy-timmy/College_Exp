# wap to create a list containing the power of said number in bases raised to the corresponding humber in the index using python map
def power_list(a):
    return list(map(lambda x, i: x ** i, a, range(len(a))))

print(power_list([2, 3, 4, 5]))