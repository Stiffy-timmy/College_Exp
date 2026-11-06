s = input("Enter a string: ")

words = s.split()
 
for i in words:
    if len(i) % 2 == 0:
        print(i)
