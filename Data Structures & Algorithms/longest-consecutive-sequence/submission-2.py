class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lcs = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            curr = num + 1
            while curr in numSet:
                curr += 1
            lcs = max(lcs, curr - num)
        
        return lcs