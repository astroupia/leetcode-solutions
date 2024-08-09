class Solution:
    def merge(self, left, right, nums):
        i = 0
        j = 0
        key = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[key] = left[i]
                i += 1
            else:
                nums[key] = right[j]
                j += 1
            key += 1 

        while i < len(left):
            nums[key] = left[i]
            i += 1
            key += 1
        
        while j < len(right):
            nums[key] = right[j]
            j += 1
            key += 1
        
        return nums
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right, nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

