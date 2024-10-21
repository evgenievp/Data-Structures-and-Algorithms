# https://leetcode.com/problems/rotate-image/description/
# rorate matrix - 90 degrees

def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    res = ''
    for row in matrix:
        res += f"{row}\n"
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(row)
print()
print(rotate(matrix))
