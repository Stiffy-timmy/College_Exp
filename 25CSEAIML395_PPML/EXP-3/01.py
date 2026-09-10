# -------------USING MULTIPLE FUNCTION--------------------
# def checkPrime(num):
#     isPrime = True
#     i = 2  #start from 2, as all number is divisible by 1
#     while i <= num / 2:
#         if num % i == 0:
#             isPrime = False
#             break
#         i += 1
#     if not isPrime:
#         print(f"{num} is NOT prime")
#         return False
#     return num


# def checkTwinPrime(a,b):
#     result_a = checkPrime(a)
#     result_b = checkPrime(b)

#     if False in [result_b, result_b]:
#         return
#     if abs(result_a - result_b) == 2:
#         return True 

# ---------USING DECORATOR----------
def checkPrime(func):
    def wrapper(*args):
        checked = []
        for arg in args:
            isPrime = True
            i = 2  #start from 2, as all number is divisible by 1
            while i <= arg / 2:
                if arg % i == 0:
                    isPrime = False
                    break
                i += 1
            if isPrime == False:
                print(f"{arg} is NOT prime")
                return func(isPrime)
            checked.append(arg)

        return func(*checked) #This is called Iterable Unpacking
    return wrapper

@checkPrime 
def checkTwinPrime(*result):
    if False in result:
        return
    print(result)
    if abs(result[0] - result[1]) == 2:
        print(abs(result[0] - result[1]))
        return True



# ---------PROGRAM STARTS HERE------------
def main():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))

    res = checkTwinPrime(a,b)
    if res:
        print(f"{a} and {b} are twin prime")

if __name__ == '__main__':
    main()