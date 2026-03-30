class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        
        for num in numSet:
            #look only for the start of an lc
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                maxLength = max(length,maxLength)
        
        return maxLength