class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lcs = 0

        for num in nums:
            if num not in numSet or num - 1 in numSet:
                continue
            curr = num + 1
            while curr in numSet:
                numSet.remove(curr)
                curr += 1
            lcs = max(lcs, curr - num)
        
        return lcs