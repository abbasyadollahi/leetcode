def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if (nums[i] + nums[j]) == target:
                print(target)
                return [nums[i], nums[j]]

nums = [2, 7, 11, 15]
target = 23
twoSum(nums, target)
