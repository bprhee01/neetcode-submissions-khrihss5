class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l,r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]

        while l < r:
            
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                trapped = max(0, maxL - height[l])
                water += trapped
            elif height[l] >= height[r]:
                r -= 1
                maxR = max(maxR, height[r])
                trapped = max(0, maxR - height[r])
                water += trapped
        

        return water