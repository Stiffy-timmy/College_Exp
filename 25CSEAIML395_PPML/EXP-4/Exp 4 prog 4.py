
n=int(input("Enter the num:"))
arr=list(input("Enter the list:"))
sum=0
sumx=0

l=len(arr)
for i in range(0,n+1):
    sum=sum+i
for i in arr:
    sumx=sumx+int(i)

if l==n+1:
    if sumx==sum:
        print("Elements:")
    else:
        print("Duplicate")
else:
    print(sum-sumx)
     