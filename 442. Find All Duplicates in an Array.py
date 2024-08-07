class Solution:
    def swap(self, nums, first, second):
        nums[first], nums[second] = nums[second], nums[first]
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Place each number in its correct index
        i = 0
        while i < len(nums):
            correctIndex = nums[i] - 1
            if nums[i] != nums[correctIndex]:
                self.swap(nums, i, correctIndex)
            else:
                i += 1
        
        # Step 2: Find duplicates
        duplicateNums = set()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicateNums.add(nums[i])
        
        return list(duplicateNums)
