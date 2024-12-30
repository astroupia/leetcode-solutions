def pivotIndex(nums):
        totalSum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        
        return -1