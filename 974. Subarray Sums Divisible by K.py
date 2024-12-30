def subArrayDivisible(nums, k):
        preFix = 0
        remainder_count = {0: 1}
        count = 0
        
        for num in nums:
            preFix += num
            remainder = preFix % k
            
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count