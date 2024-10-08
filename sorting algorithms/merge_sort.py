import random_numbers

arr = random_numbers.fill_with_random_numbers()


def merge_sort(arr):
    if len(arr) > 1:
        left_part = arr[:len(arr) // 2]
        right_part = arr[len(arr) // 2:]

        merge_sort(left_part)
        merge_sort(right_part)

        i, j, k = 0, 0, 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

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
