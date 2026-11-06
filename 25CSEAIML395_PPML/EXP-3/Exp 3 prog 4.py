x = input("Enter a string:")

if x == x[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

if x[:len(x)//2] == x[len(x)//2:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")
