class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxStack = deque()
        output = []
        l,r = 0,0

        while r < len(nums):
            curr = nums[r]

            while len(maxStack) and nums[maxStack[-1]] < curr:
                maxStack.pop()
            maxStack.append(r)

            if (r - l + 1) == k:
                print(l,r)
                output.append(nums[maxStack[0]])
                l += 1
            r += 1

            while len(maxStack) and maxStack[0] < l:
                maxStack.popleft()
        
        return output
            
