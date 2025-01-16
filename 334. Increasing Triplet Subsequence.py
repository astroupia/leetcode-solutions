def increasingTriplet(nums):
    first, second = float('inf'), float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
