class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #list of integers
        #return an array where array[i] is the length from i to an arbitrary n when list[n] > list[i]

        output = [0 for i in range(len(temperatures))]
        stack = []

        for idx, temp in enumerate(temperatures):
            while len(stack) and stack[-1][1] < temp:
                prevI = stack.pop()[0]
                print(prevI)
                output[prevI] = idx - prevI
            stack.append((idx,temp))
        
        return output
