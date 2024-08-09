class Solution:
    def swap(self, nums, first, second):
            nums[first] , nums[second] = nums[second], nums[first]

    def moveZeroes(self, nums: List[int]) -> None:
        correct = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(nums, i, correct)
                correct += 1
            

        