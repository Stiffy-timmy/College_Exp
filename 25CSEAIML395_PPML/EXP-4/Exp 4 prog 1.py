arr=[]
x=int(input("Enter a element:"))

for i in range(x):
    m=int(input("Enter the elements into array:"))
    arr.append(m)
print("This is original list:",arr)

for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1] = arr[k+1],arr[k]
print("Sorted array:",arr)

print("Second largest:",arr[-2])
print("Second smallest:",arr[1])
