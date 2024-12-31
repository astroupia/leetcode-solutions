def oceanView(nums):
    result = []
    maxBuilding = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > maxBuilding:
            result.append(i)
            maxBuilding = nums[i]
    return result[::-1]