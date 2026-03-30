class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN = float('inf')

        l,r = 0,len(nums) - 1

        while l <= r :
            m = l + (r - l ) // 2
            minN = min(minN,nums[m])

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return minN
