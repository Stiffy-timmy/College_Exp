# WAP to convert all the characters into uppercase and lowercase and eliminate duplicates letters from a given sequence. use MAp() function
def convert(s):
    u = ''.join(dict.fromkeys(map(str.upper, s)))
    l = ''.join(dict.fromkeys(map(str.lower, s)))
    return u, l

print(convert("Programming"))