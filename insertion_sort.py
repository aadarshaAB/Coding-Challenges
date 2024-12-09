def insert_sort(numbers):
    n = len(numbers)
    for i in range(1,n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j = j - 1
        numbers[j+1] = key
    return numbers
a = [2, 4, 1, 5, 9, 6]
print(f"Sorted list is {insert_sort(a)}")
