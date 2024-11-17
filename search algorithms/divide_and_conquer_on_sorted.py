import random_numbers


arr = random_numbers.fill_with_random_numbers()
arr.sort()


def find_num(arr, n):
    if n > arr[-1]:
        return - 1
    if arr[-1] == n:
        return arr[-1]
    if len(arr) <= 1:
        return -1

    first_part, second_part = arr[:len(arr) // 2], arr[len(arr) // 2:]

    if n > first_part[-1]:
        return find_num(second_part, n)
    else:
        return find_num(first_part, n)


arr.sort()

print(find_num(arr, 10))
