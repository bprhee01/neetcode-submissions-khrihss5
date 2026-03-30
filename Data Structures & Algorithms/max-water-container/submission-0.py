class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        currArea = 0

        #brute force approach
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                currArea = (j - i ) * min(heights[i],heights[j])
                maxArea = max(maxArea,currArea)

        return maxArea