class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        firstStringDict = {}
        for char in s:
            if char not in firstStringDict:
                firstStringDict[char] = 1
            else:
                firstStringDict[char] += 1
        
        for char in t:
            if char not in firstStringDict:
                return False
            elif firstStringDict[char] == 0:
                return False
            else:
                firstStringDict[char] -= 1
        

        return True