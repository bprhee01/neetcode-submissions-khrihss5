class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0,1
        maxSum = nums[0]
        currSum = nums[0]

        while r < len(nums):
            if currSum < 0:
                currSum = 0
                l = r
            currSum += nums[r]
            maxSum = max(maxSum, currSum)
            r += 1

        return maxSum