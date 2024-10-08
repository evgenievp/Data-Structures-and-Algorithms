# Implementation of elementary recursion which sums all numbers up to given number.

def recursiveRange(num):
    if num <= 1:
        return num
    return recursiveRange(num - 1) + num


print(recursiveRange(6)) # 21
