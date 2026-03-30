class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        l,r = 0,0

        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(s[r])
            print(l,r)
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans