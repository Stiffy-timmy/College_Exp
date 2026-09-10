
arr = [item for item in range(1,21)]
print("Array: ", arr)
for idx in range(len(arr)):
    if arr[idx] % 2 != 0:
        arr[idx] = arr[idx] + 5
print("Array: ", arr)
