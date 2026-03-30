class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        sum = 0
        l,r = 0,0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                minLength = min(minLength, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        
        if minLength == len(nums) + 1:
            return 0
        return minLength