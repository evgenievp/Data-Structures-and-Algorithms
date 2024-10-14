# https://leetcode.com/problems/single-number/description
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


nums = [4, 1, 2, 1, 2]
# Beats 44% of solutions.
print(singleNumber(nums)) # 4
