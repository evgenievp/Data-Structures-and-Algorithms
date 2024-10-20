n = input()
n = str(n)
n = n.replace(".", "")
n = n.replace("-", "")

def sum_digits(n):
    res = 0
    n = str(n)
    for i in range(len(n)):
        res += int(n[i])
    return res
n = int(n)
while n > 9:
    n = sum_digits(n)
print(n)

