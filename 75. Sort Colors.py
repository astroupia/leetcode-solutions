class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return nums
        
        maxVal = max(nums)

        freq = [0] * (maxVal + 1)

        for i in nums:
            freq[i] += 1
        
        index = 0
        for i in range(len(freq)):
            while freq[i] > 0:
                nums[index] = i
                index += 1
                freq[i] -= 1
        return nums
        