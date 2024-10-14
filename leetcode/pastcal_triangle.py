def pascal_triangle(numRows):
    arr = [[1], [1, 1]]
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    for i in range(3, numRows + 1):
        row = [1]
        last_row = arr[-1]
        for idx in range(len(arr[-1]) - 1):
            val = last_row[idx] + last_row[idx + 1]
            row.append(val)
        row.append(1)
        arr.append(row)
    return arr


print(pascal_triangle(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
