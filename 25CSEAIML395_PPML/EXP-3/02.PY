def factorial(num):
    if num < 1 :
        return 1
    else:
        return num * factorial (num - 1)

def main():
    num = int(input("Enter Number: "))
    result = factorial(num)
    print(f"Factorial of {num}: {result}")


if __name__ == "__main__":
    main()