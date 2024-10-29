# https://leetcode.com/problems/missing-number/submissions/1437353606/?envType=problem-list-v2&envId=array

def missingNumber(nums, list) -> int:
    for n in range(0, len(nums) + 1):
        if n not in nums:
            return n


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
missingNumber(nums)  # 8
