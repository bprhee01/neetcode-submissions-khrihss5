import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l,r=  1,piles[-1]
        k = r

        while l <= r:
            m = l + (r - l) // 2
            hCount = 0
            i = 0
            while hCount <= h and i < len(piles):
                hCount += math.ceil(piles[i] / m )
                i += 1
            
            if hCount <= h:
                k = min(k,m)
                r = m -1
            else:
                l = m + 1


        return k