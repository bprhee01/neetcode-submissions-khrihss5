class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = set()
        l,r = 0,0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen and l < r:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength

