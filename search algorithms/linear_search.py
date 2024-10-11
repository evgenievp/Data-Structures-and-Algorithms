import random_numbers
import random


def linear_search(arr, item):
    for element in arr:
        if element == item:
            return element
    return - 1


arr = random_numbers.fill_with_random_numbers()
idx = random.randint(0, len(arr) - 1)
item = arr[idx]
print(f"Searched item {item}")
print(linear_search(arr, item))

