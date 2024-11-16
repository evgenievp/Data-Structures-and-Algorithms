import random_numbers

arr = random_numbers.fill_with_random_numbers()


def sort(arr, n):
    if len(arr) == 1:
        return arr

    arr1, arr2 = arr[:len(arr) // 2], arr[len(arr) // 2:]

    if n in arr1:
        return sort(arr1, n)
    if n in arr2:
        return sort(arr2, n)
    else:
        return -1


arr = sort(arr, 10)
print(arr)
