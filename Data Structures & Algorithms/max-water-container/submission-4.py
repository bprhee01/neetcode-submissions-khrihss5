class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) - 1

        maxA = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

            curr =min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, curr)


        return maxA