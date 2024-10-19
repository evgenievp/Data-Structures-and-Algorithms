def heapify(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[l] < array[smallest]:
        smallest = l

    if r < n and array[r] < array[smallest]:
        smallest = r

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)


def heap_sort(array):
    n = len(array)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heap_sort(cList)
print(cList)
