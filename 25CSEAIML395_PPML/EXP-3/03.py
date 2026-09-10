
def checkSymmetric(string):
    count = len(string)
    mid = count // 2
    if count % 2 == 0:
        print("Even String")
        if string[0 : int(mid)] == string[int(mid) : ]:
            print(f"{string.upper()} is Symmetric")
        else:
            print(f"{string.upper()} is NOT Symmetric")
    else:
        print("Odd String")
        if string[:mid] == string[mid + 1:]:
            print(f"{string.upper()} is Symmetric")
        else:
            print(f"{string.upper()} is NOT Symmetric")

def checkPalindrome(string):
    if string == string[::-1]:
        print("String is Palindrome")
    else:    
        print("String is NOT Palindrome")    

def main():
    string = input("Enter Word: ")
    checkPalindrome(string)
    checkSymmetric(string)

if __name__ == "__main__":
    main()