class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(soFar:List[int], sum, i):
            if sum == target:
                ans.append(soFar.copy())
                return
            if sum > target or i > len(nums) - 1:
                return
            soFar.append(nums[i])
            helper(soFar, sum + nums[i], i)
            soFar.pop()
            helper(soFar.copy(), sum, i + 1)
        helper([],0, 0)
        return ans