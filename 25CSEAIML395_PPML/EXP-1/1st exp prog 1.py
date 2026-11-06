
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)
    print("Modulus =", num1 % num2)
else:
    print("Division, Floor Division, and Modulus cannot be performed because the second number is 0.")

print("Exponentiation =", num1 ** num2)
