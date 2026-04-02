class Solution:
    def climbStairs(self, n: int) -> int:
        oneBack, twoBack = 1,1
        curr = 1
        for stair in range(1,n):
            curr = oneBack + twoBack
            twoBack = oneBack
            oneBack = curr
        return curr

