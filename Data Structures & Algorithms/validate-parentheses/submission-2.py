class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            elif not stack:
                return False
            elif mapping[stack[len(stack)-1]] == c:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True

