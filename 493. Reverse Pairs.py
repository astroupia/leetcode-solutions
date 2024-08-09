class Solution:
    def __init__(self):
        self.count = 0

    def revPair(self, left, right):
        i = 0
        j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] > 2 * right[j]:
                count += len(left) - i
                j += 1
            else:
                i += 1
        return count

    def merge(self, nums, leftSide, rightSide):
        leftPointer = 0
        rightPointer = 0
        key = 0

        while leftPointer < len(leftSide) and rightPointer < len(rightSide):
            if leftSide[leftPointer] <= rightSide[rightPointer]:
                nums[key] = leftSide[leftPointer]
                leftPointer += 1
            else:
                nums[key] = rightSide[rightPointer]
                rightPointer += 1
            key += 1

        while leftPointer < len(leftSide):
            nums[key] = leftSide[leftPointer]
            leftPointer += 1
            key += 1

        while rightPointer < len(rightSide):
            nums[key] = rightSide[rightPointer]
            rightPointer += 1
            key += 1

    def sort(self, nums):
        if len(nums) <= 1:
            return

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        self.sort(left)
        self.sort(right)

        self.count += self.revPair(left, right)

        self.merge(nums, left, right)

    def reversePairs(self, nums: List[int]) -> int:
        self.sort(nums)
        return self.count
