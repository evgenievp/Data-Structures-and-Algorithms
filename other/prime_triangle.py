def is_prime(n):
    if n <= 1:
        return True
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
n = int(input())
array = []

for i in range(1, n + 1):
    if is_prime(i):
        array.append(i)

for i in range(len(array)):
    row = ''
    for j in range(1, array[i] + 1):
        if is_prime(j):
            row += "1"
        else:
            row += "0"
    print(row)