total = 0
while True:
    num = str(input())

    middle = int(num[1])
    first = int(num[0])
    last = int(num[2])
    if middle == (first + last):
        total += int(num)
        continue
    else:
        print(total)
        break
