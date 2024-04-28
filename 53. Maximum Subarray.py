class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxCrossingSum(nums, left, mid, right):
            leftSum = float('-inf')
            rightSum = float('-inf')
            tempSum = 0

            for i in range(mid, left - 1, -1):
                tempSum += nums[i]
                leftSum = max(leftSum, tempSum)

            tempSum = 0
            for i in range(mid + 1, right + 1):
                tempSum += nums[i]
                rightSum = max(rightSum, tempSum)

            return leftSum + rightSum

        def maxSubArrayHelper(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            leftMax = maxSubArrayHelper(nums, left, mid)
            rightMax = maxSubArrayHelper(nums, mid + 1, right)
            crossingMax = maxCrossingSum(nums, left, mid, right)

            return max(leftMax, rightMax, crossingMax)

        return maxSubArrayHelper(nums, 0, len(nums) - 1)
        