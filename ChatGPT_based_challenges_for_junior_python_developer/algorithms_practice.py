def two_sum(nums: list[int], target: int) -> list[int]:
    # Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    results = []
    j = len(nums) - 1
    for i in range(len(nums) - 1):
        if nums[i] > target:
            continue
        else:
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    results.append(i)
                    results.append(j)

    return results


nums = [2, 7, 11, 15, 6, 3]
target = 9
print(two_sum(nums, target))
