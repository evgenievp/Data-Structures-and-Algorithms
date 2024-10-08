import random_numbers

arr = random_numbers.fill_with_random_numbers()


def merge_sort(arr):
    if len(arr) > 1:
        # divide array into two parts
        left_part = arr[:len(arr) // 2]
        right_part = arr[len(arr) // 2:]

        # recursive call for both parts of array.
        merge_sort(left_part)
        merge_sort(right_part)

        # three variables for indexes
        i, j, k = 0, 0, 0

        # main loop of merge sort. Append elements to right or left of the table
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # two sub loops for the same thing.
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1


merge_sort(arr)
print(arr)
