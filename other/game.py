n = int(input())
def sum_digits(n):
    n = str(n)
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    return res


def multiplication(n):
    n = str(n)
    if "0" in n:
        n.replace("0", "")
    res = 1


    return res


num1 = sum_digits(n)
num2 = multiplication(n)
if num2 > num1:
    print(num2)
else:
    print(num1)
