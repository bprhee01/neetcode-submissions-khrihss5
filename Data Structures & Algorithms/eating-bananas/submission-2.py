import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        minK = r

        while l <= r:
            k = l + (r -  l) // 2
            hDone = 0
            
            for pile in piles:
                hDone += math.ceil(pile / k)
            if hDone <= h:
                minK = k
                r = k -1
            else :
                l = k + 1

        return minK

        