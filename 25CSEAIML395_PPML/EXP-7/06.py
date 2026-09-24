# WAP to find the ratio of positive numbers negative numbers and zero is an array
def ratio(a):
    p = sum(map(lambda x: x > 0, a))
    n = sum(map(lambda x: x < 0, a))
    z = sum(map(lambda x: x == 0, a))
    l = len(a)
    return p/l, n/l, z/l

print(ratio([1, -2, 0, 3, -4, 0]))