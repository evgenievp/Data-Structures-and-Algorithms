#https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=array
def find_third_max(nums):
    n = len(nums)
    result = 0
    first = max(nums)
    second = min(nums)
    third = float("-inf")

    for i in range(n):
        if nums[i] < first and nums[i] > second:
            third = second
            second = nums[i]
        elif nums[i] < second and nums[i] > third:
            third = nums[i]
        else:
            pass
    if len(set(nums)) >= 3:
        result = third
    else:
        result = first
    return result


