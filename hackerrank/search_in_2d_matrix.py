#https://leetcode.com/problems/search-a-2d-matrix

def search_matrix(matrix, target):
    traverse_row = []
    answer = 'false'
    for idx in range(0, len(matrix) - 1):
        row = matrix[idx]
        if row[0] <= target < matrix[idx + 1][0]:
            traverse_row = row
            break
    if not traverse_row and matrix[-1][0] <= target:
        traverse_row = matrix[-1]

    i, j = 0, len(traverse_row) - 1
    while i <= j:
        if traverse_row[i] == target or traverse_row[j] == target:
            answer = 'true'
            return answer
        i += 1
        j -= 1
    return answer


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(search_matrix(matrix, 13)) # false


