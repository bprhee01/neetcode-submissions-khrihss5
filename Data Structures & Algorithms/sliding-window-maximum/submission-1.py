import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        maxValsIndex = deque()
        l,r = 0,0

        while r < len(nums):
            cur = nums[r]
            
            while maxValsIndex and nums[maxValsIndex[-1]] < cur:
                maxValsIndex.pop()
            maxValsIndex.append(r)

            if maxValsIndex[0] < l:
                maxValsIndex.popleft()

            if (r - l + 1) == k:
                output.append(nums[maxValsIndex[0]])
                l += 1
            r += 1
        
        return output
                

