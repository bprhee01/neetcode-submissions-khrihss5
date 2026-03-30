class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            if char not in countS:
                countS[char] = 0
            countS[char] += 1
        
        for char in t:
            if char not in countT:
                countT[char] = 0
            countT[char] += 1

        if len(countS) != len(countT):
            return False

        for char in countS:
            if char not in countT:
                return False
            if countS[char] != countT[char]:
                return False
        

        return True