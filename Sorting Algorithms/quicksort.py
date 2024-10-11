import random_numbers
arr = random_numbers.fill_with_random_numbers()

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop() # our pivot in worst case - last element
    right_part_arr, left_part_arr = [], [] # Two arrays - for lower part of array and for higher.

    for el in arr: # loop which append elements to lower and higher arrays, compared with pivot
        if el > pivot:
            right_part_arr.append(el)
        else:
            left_part_arr.append(el)

    return quicksort(left_part_arr) + [pivot] + quicksort(right_part_arr)


print(quicksort(arr))

