# beats 88.35 from all solutions
def digits_plus(digits):
    n = ''
    for num in digits:
        n += str(num)
    num = int(n) + 1
    arr = [int(digit) for digit in str(num)]
    return arr


arr = [1, 2, 3]
print(digits_plus(arr)) # [1, 2, 4]
# https://leetcode.com/problems/plus-one