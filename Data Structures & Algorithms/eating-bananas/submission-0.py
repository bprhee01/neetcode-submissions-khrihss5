import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        for k in range(1,max(piles) + 1):
            hDone = 0
            i = 0
            while hDone <= h and i < len(piles):
                hDone += math.ceil(piles[i] / k)
                i += 1
            if h < hDone:
                continue
            return k