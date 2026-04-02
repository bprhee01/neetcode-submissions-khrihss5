class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        #make an array that holds is the length of nums * target
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(len(nums)):
            for currentTarget in range(target+1):
                dp[i][currentTarget] = dp[i-1][currentTarget-nums[i]] or dp[i-1][currentTarget]
        return dp[len(nums)-1][target]

