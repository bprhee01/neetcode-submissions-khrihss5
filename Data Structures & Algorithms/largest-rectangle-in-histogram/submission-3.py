#scenarios
#always ascending 1,2,3,4,5
    #never pop off tha stack
    #at the end loop from that position to the end with that height
#always descending # 5 4 3 2 1
    # you know a min of 1 expands for all, so when storing 1 you should include 0 as your staer
    # for 3 its start is also at 3

# 3 7 9 6 3


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        minStack = []

        for i, height in enumerate(heights):
            if not len(stack):
                stack.append(i)
                minStack.append(height)
            else:
                if minStack[-1] < height:
                    stack.append(i)
                    minStack.append(height)
                lastPop = stack[-1]
                while len(stack) and minStack[-1] > height:
                    largest = max(largest, minStack[-1] * (i - stack[-1]))
                    lastPop = stack[-1]
                    minStack.pop()
                    stack.pop()
                stack.append(lastPop)
                minStack.append(height)
        
        while len(stack):
            currArea = (len(heights) - stack.pop()) * minStack.pop()
            largest = max(largest,currArea)




    
        return largest


         