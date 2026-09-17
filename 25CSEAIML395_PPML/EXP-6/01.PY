rows = 3
columns = 3

matrix = []
newMatrix = []
numberTypeCount = {}

# Create original matrix and count numbers
for i in range(rows):
    row = []

    for j in range(columns):
        n = int(input("Enter Number: "))

        if n not in numberTypeCount:
            numberTypeCount[n] = 1
        else:
            numberTypeCount[n] += 1

        row.append(n)

    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(*row)

print("Number Count:", numberTypeCount)


# Create grouped matrix
row = []

for number, count in numberTypeCount.items():
    for ct in range(count):
        row.append(number)

    # Once we have enough elements for a row,
    # put it into newMatrix
    while len(row) >= columns:
        newMatrix.append(row[:columns])
        row = row[columns:]


print("New Matrix:")
for row in newMatrix:
    print(*row)

# if matrix[i][j] in numberTypeCount:
#             print(f"yes matrix[{i}][{j}] = {matrix[i][j]} and dict = {numberTypeCount[matrix[i][j]]}")