class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []
        i = 0
        while i < len(temperatures):
            if not stack or  temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            elif  temperatures[stack[-1]] < temperatures[i]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                    print(result)
                stack.append(i)
            i += 1
        return result
