def find_duplicate(nums):
    if not nums:
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False

        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
