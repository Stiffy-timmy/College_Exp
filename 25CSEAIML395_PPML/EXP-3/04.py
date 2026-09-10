def remove_duplicates(input_string):
    result = ""

    for index, character in enumerate(input_string):

        # Check whether the character has appeared before
        if character not in input_string[:index]:
            result = result + character

    return result


# Driver code
string = input("Enter a string: ")

output = remove_duplicates(string)

print("String after removing duplicates:", output)