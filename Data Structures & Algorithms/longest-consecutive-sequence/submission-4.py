class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        startSeqNums = []
        seen = set()
        lcs = 0

        for num in nums:
            if num - 1 not in seen:
                startSeqNums.append(num)
            seen.add(num)
        
        for num in startSeqNums:
            counter = 1
            while num + 1 in seen:
                counter += 1
                num += 1
            
            if counter > lcs:
                lcs = counter
            
        return lcs