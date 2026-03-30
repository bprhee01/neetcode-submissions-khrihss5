class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax, currMax = nums[0], float('-inf')

        for num in nums:
            currMax = max(currMax + num, num)
            globalMax = max(globalMax, currMax)
        
        return globalMax
