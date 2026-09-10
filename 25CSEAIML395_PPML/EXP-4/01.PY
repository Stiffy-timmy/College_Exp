def bubble_sort(array, n):
    for item in range(n):
        for comp in range(n - item - 1):
            if array[comp] > array[comp + 1]:
                temp = array[comp]
                array[comp] = array[comp + 1]
                array[comp + 1] = temp

    return array
                
            
def main():
    n = int(input("Enter Number of Elements to Enter: "))
    arr = []

    for i in range(n):
        temp = int(input(f"Enter Element {i + 1}: "))
        arr.append(temp)

    print("Array:  ", arr)
    sorted_array = bubble_sort(arr, n)
    print("Sorted Array: ", sorted_array)
    print("2nd Largest: ", sorted_array[n-2])
    print("2nd smallest: ", sorted_array[1])
if __name__ == "__main__":
    main()