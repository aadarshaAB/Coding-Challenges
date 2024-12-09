def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr     

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [2, 4, 1, 5, 9, 6]    
    print("Sorted array is:",bubbleSort(arr))