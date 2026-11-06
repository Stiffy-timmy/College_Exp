list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]

string = []

for i in range(len(list1)):
    string.append(str(list1[i]))
    string.append(list2[i])

print(string)
