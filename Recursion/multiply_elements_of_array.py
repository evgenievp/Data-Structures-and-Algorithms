def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


arr = [1, 2, 2, 5, 8]
print(productOfArray(arr)) # 160