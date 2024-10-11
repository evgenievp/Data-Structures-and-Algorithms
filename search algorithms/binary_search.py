import math
import random
import random_numbers


def binary_search(array, value):
    start_idx = 0
    end_idx = len(array) - 1
    middle = math.floor(end_idx / 2)
    while array[middle] != value and start_idx <= end_idx:
        if value < array[middle]:
            end_idx = middle - 1
        else:
            start_idx = middle + 1
        middle = math.floor((start_idx + end_idx) / 2)
    if array[middle] == value:
        return f"Searched value is in {middle} idx. And its value is: {array[middle]}"
    else:
        return -1


arr = random_numbers.fill_with_random_numbers()
idx = random.randint(0, len(arr))
value = arr[idx]
arr.sort() # always array have to be sorted. Binary search works only with sorted array.
print(binary_search(arr, value))

