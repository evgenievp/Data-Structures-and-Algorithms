# https://leetcode.com/problems/contains-duplicate/?envType=problem-list-v2&envId=array
def containsDuplicate(nums: list[int]) -> bool:
    dict = {}

    for el in nums:
        if el not in dict:
            dict[el] = 1
        else:
            return True
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # True
