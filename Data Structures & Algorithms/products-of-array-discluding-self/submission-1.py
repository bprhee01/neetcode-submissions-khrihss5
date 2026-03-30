class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        total = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                total *= num
        if zeroCount > 1:
            return output
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                output[i] = total
            elif zeroCount == 1:
                output[i] = 0
            else:
                output[i] = total // nums[i]
            i += 1
        
        return output