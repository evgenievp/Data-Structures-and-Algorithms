arr = []
for i in range(1, 11):
    arr.append(i)

print(arr)


def rotate_array(arr, k):
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr


arr = rotate_array(arr, 3)
print(arr)
