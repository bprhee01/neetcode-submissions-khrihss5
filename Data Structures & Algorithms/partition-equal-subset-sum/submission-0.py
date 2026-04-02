class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        
        if total % 2 != 0:
            return False
        
        target = total  / 2

        sums = set()
        sums.add(0)

        for num in nums:
            prevSums = sums.copy()
            for curSum in prevSums:
                if target == curSum + num:
                    return True
                sums.add(curSum + num)
        return False
        
         