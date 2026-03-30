class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = [0] * 26
        tMap = [0] * 26
        for char in s:
            sMap[ord(char)-97] += 1
        for char in t:
            tMap[ord(char)-97] += 1
        
        for char in range(26):
            if sMap[char] != tMap[char]:
                return False
        return True