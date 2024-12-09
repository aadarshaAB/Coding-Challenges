def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[k] = left [i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1
    while i< len(left):
        result[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1
    
    return result

if __name__ == "__main__":
    arr = [2, 4, 1, 5, 9, 6]
    print(f"Sorted Array:{mergeSort(arr)}")

