class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Chars = {}
        cUsed = 0
        for c in s1:
            s1Chars[c] = 1 + s1Chars.get(c,0)

        l,r = 0,0

        while r < len(s2):
            print(s1Chars)
            if s2[r] not in s1Chars:
                while l < r:
                    s1Chars[s2[l]] += 1
                    cUsed -= 1
                    l += 1
                r += 1
                l = r
            elif s1Chars[s2[r]] == 0:
                while s1Chars[s2[r]] == 0:
                    s1Chars[s2[l]] += 1
                    cUsed -= 1
                    l += 1
                s1Chars[s2[r]] -= 1
                cUsed += 1
                r += 1
            else:
                s1Chars[s2[r]] -= 1
                r += 1
                cUsed += 1
                if cUsed == len(s1):
                    return True
        
        return False

