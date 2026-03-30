class Solution:
    class Node:
        def __init__(self, height, index):
            self.height = height
            self.index = index

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        for index,height in enumerate(heights):
            #case where height is larger or equal than last item in stack
            if not len(stack) or stack[-1].height <= height:
                stack.append(self.Node(height,index))
            #case where it's smaller
            else:
                lastIndex = index
                while len(stack) and height < stack[-1].height:
                    maxArea = max(maxArea,(stack[-1].height) * (index - stack[-1].index))
                    lastIndex = stack[-1].index
                    stack.pop()
                stack.append(self.Node(height,lastIndex))
        
        while len(stack):
            maxArea = max(maxArea,stack[-1].height * (len(heights) - stack[-1].index))
            stack.pop()



        return maxArea
