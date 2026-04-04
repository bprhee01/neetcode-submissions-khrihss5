class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeros = 0
        zeroIdx = 0
        for i,num in enumerate(nums):
            if num == 0:
                numZeros += 1
                zeroIdx = i
            else:
                totalProduct *= num

        ans = [0 for _ in range(len(nums))]
        if numZeros >= 2:
            return ans
        if numZeros == 1:
            ans[zeroIdx] = totalProduct
            return ans

        for i,num in enumerate(nums):
            ans[i] = totalProduct // num
        return ans