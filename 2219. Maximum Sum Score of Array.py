def maxSumScore(nums):
    prefix = 0
    suffix = sum(nums)
    maxScore = 0 
    
    for num in nums:
        prefix += num
        maxScore = max(maxScore, prefix, suffix - prefix + num)
    return maxScore