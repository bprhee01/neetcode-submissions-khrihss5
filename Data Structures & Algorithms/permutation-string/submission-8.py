class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freq = defaultdict(int)
        s2Freq = defaultdict(int)
        for c in s1:
            s1Freq[c] += 1
        
        for i in range(len(s1)):
            s2Freq[s2[i]] += 1
        
        l,r = 0, len(s1) - 1
        while r < len(s2):
            # print(s2Freq)
            if s1Freq == s2Freq:
                return True
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                s2Freq.pop(s2[l])
            l += 1
            r += 1
            if r >= len(s2):
                continue
            s2Freq[s2[r]] += 1
        return False
            