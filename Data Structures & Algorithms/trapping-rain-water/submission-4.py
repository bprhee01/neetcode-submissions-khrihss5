class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        maxTrapped = [0 for i in range(len(height))]

        l,r = 0,1
        while r < len(height):
            if height[l] <= height[r]:
                curr = l + 1
                while curr < r:
                    maxTrapped[curr] = max(height[l] - height[curr], maxTrapped[curr])
                    curr += 1
                l = r
                r += 1
            else:
                r += 1
        
        l,r = len(height) - 2, len(height) - 1

        while -1 < l:
            if height[l] >= height[r]:
                curr = r - 1
                while curr > l:
                    maxTrapped[curr] = max(height[r] - height[curr], maxTrapped[curr])
                    curr -= 1
                r = l
                l -= 1
            else:
                l -= 1
        
        return sum(maxTrapped)
