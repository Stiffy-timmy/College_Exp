str = []
x=int(input("Enter the number of elements:"))
for i in range(x):
    n=int(input("Enter thr element:"))
    str.append(n)

for i in range(x):
    if str[i]%2!=0:
        str[i]=str[i]+5

print(str)        
