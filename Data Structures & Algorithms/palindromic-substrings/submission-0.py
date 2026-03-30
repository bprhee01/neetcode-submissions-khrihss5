class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def palindrome(l,r):
            print('here',l,r)
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            ans += palindrome(i,i+1) + palindrome(i,i)
        
        return ans