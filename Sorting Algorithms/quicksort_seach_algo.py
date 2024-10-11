import random_numbers
import random


# my version of divide and conquer algorithm.
def quicksort_search(arr, item):
    if len(arr) == 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    if item in left:
        return quicksort_search(left, item)
    return quicksort_search(right, item)


arr = random_numbers.fill_with_random_numbers()

item = arr[random.randint(0, len(arr))]
print(f"Searched item {item}")

print(quicksort_search(arr, item))
