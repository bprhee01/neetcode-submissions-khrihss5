class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        l,r = 0, 0

        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
            max_length = max(max_length,(r-l+1))
            seen.add(s[r])
            r += 1
        
        return max_length