n = int(input("Enter a number:"))

for i in range(2, n):
    a = 0
    b = 0

    for j in range(1, i + 1):
        if i % j == 0:
            a += 1

    for j in range(1, i + 3):
        if (i + 2) % j == 0:
            b += 1

    if a == 2 and b == 2:
        print(i, i + 2)
