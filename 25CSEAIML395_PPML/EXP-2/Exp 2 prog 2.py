num = input("Enter a 5 digit number: ")

if len(num) == 5:
    print("Digits at odd positions are:", num[0], num[2], num[4])
else:
    print("Please enter a valid number:")
