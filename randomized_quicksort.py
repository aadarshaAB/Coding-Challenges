import numpy as np


def partition(arr, p, r):
    pivot_id = np.random.randint(p,r+1)
    arr[pivot_id],arr[r] = arr[r], arr[pivot_id]
    pivot = arr[r]
    i = p - 1
    for j in range(p,r):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, r)
    return i+1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def randQuickSort(arr, p, r):
    if p < r:
        par = partition(arr, p, r)

        randQuickSort(arr, p, par-1)
        randQuickSort(arr, par+1, r)

if __name__ == "__main__":
    arr = [2, 4, 1, 5, 9, 6]
    n = len(arr)

    randQuickSort(arr, 0, n-1)

    for val in arr:
        print(val, end=" ")