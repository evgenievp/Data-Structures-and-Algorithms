import random_numbers


arr = random_numbers.fill_with_random_numbers()

# Bubble sort
for idx in range(len(arr)):
    for idx_b in range(idx, len(arr)):
        if arr[idx] > arr[idx_b]:
            arr[idx], arr[idx_b] = arr[idx_b], arr[idx]

print(arr)