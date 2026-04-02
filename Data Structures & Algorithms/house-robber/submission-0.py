class Solution:
    def rob(self, nums: List[int]) -> int:
        oneBack, twoBack = 0,0

        for num in nums:
            temp = oneBack
            oneBack = max(twoBack + num, oneBack)
            twoBack = temp
        return oneBack
