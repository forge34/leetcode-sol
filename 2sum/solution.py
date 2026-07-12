def twoSum(nums: list[int], target: int) -> list[int]:

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue

            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(twoSum([2, 7, 11, 15], 9))
